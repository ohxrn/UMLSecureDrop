import socket
import ssl
from addRequest import addReq
from addRequest import newFriend


def initiateBackend(my_email):
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(
        certfile="/app/docker_content/tls/server.pem",
        keyfile="/app/docker_content/tls/server.key"
    )

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 9999))
    server.listen(5)

    while True:
        client_socket, client_address = server.accept()
        tls_socket = context.wrap_socket(client_socket, server_side=True)

        data = tls_socket.recv(1024)
        message = data.decode()

        if message.startswith("WHO|"):
            tls_socket.send(("HERE|" + my_email).encode())

        elif message.startswith("FR|"):
            sender_email = message.split("|")[1]

            result = addReq(sender_email, my_email)

            if result == 1:
                tls_socket.send(("REQUEST_RECEIVED|" + sender_email).encode())
            else:
                tls_socket.send("REQUEST_FAILED".encode())

        elif message.startswith("MERGEFRIENDS|"):
            sender_email = message.split("|")[1]

            result = newFriend(my_email,sender_email)

            if result == 1:
                tls_socket.send(("Merge_COMPLETED|" + sender_email).encode())
            else:
                tls_socket.send("MERGE_FAILED".encode())
        elif message.startswith("FILE|"):
            parts = message.split("|")
            sender_email = parts[1]
            filename = parts[2]
            print(f"{sender_email} wants to send a file: {filename}")
            ans = input("Accept file? (y/n): ")
            if ans != "y":
                tls_socket.send("DENY".encode())
            else:
                tls_socket.send("ACCEPT".encode())
                savePath = "/app/data/"+filename

                with open(savePath, "wb") as f:
                    while True:
                        bits = tls_socket.recv(4096)
                        if not bits:
                            break
                        f.write(bits)
                    print("File received:", savePath)

        else:
            print("Message:", message)
            tls_socket.send("TLS RECEIVED".encode())

        tls_socket.close()