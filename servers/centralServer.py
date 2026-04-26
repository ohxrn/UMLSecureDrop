import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("0.0.0.0",9999))
server.listen(5)

print("-----------centralC now listening------------")
while True:
        try:
            client_socket, client_address = server.accept()
            print(client_address, "joined the session")
            data = client_socket.recv(1024)
            print("Message:", data.decode())

        except KeyboardInterrupt:
            client_socket.close()
            server.close()
            print('\nServer stopped.')
            break

