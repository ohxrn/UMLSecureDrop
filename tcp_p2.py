import socket
import threading


def create_tcp_socket(server_ip, server_port):
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind((server_ip, server_port))

    tcp_socket.listen(10)  # listen for a maximum of 10 connections

    return tcp_socket


def start_client_handler_thread(client_socket):
    thread = threading.Thread(
            target=handle_client,
            args=(client_socket,)
    )
    thread.start()


def handle_client(client_socket):
    data = client_socket.recv(1024)
    print(f'Received from {client_socket}: {data}')

    client_socket.send(data)

    client_socket.close()


def main():
    server_ip = '0.0.0.0'  # listen on all interfaces
    server_port = 9999

    tcp_socket = create_tcp_socket(server_ip, server_port)
    print(f'Server is running on {server_ip}:{server_port}')

    while True:
        try:
            client_socket, client_address = tcp_socket.accept()
            print(f'New connection from {client_address}')

            start_client_handler_thread(client_socket)

        except KeyboardInterrupt:
            print('\nServer stopped.')
            break

    tcp_socket.close()


if __name__ == "__main__":
    main()
