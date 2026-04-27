import socket
import ssl
from addRequest import addReq


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

        else:
            print("Message:", message)
            tls_socket.send("TLS RECEIVED".encode())

        tls_socket.close()