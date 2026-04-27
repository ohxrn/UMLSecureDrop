import socket

def initiateBackend():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind(("0.0.0.0",9999))
    server.listen(5)

    print("-----------listener now active------------")
    while True:
        try:
            client_socket, client_address = server.accept()
            print(client_address, "joined the session")
            data = client_socket.recv(1024)
            print("Message:", data.decode())
            client_socket.send("RECEIVED".encode())
            client_socket.close()


        except KeyboardInterrupt:
            server.close()
            print("stopped")
            break