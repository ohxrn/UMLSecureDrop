import os
import socket
import time

server_ip = os.getenv('TCP_SERVER_IP', '127.0.0.1')
server_port = int(os.getenv('TCP_SERVER_PORT', '9999'))

message = os.getenv('TCP_MESSAGE')
if message is None:
    message = input("Enter a message: ")

data = message.encode('utf-8')


while True: 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_socket:
        try:
            tcp_socket.connect((server_ip, server_port))
        except ConnectionRefusedError:
            print(f"Connection refused by {server_ip}:{server_port}; retrying...")
            time.sleep(1)
            continue

        tcp_socket.send(data)

        data = tcp_socket.recv(1024)
        print(f"Received from server: {data}")

        time.sleep(1)
