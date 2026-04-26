import socket
import ssl
import threading
 

def create_tcp_socket(server_ip, server_port):
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind((server_ip, server_port))

    tcp_socket.listen(10)  # listen for a maximum of 10 connections

    return tcp_socket


def load_ssl_context():
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile="server.pem", keyfile="server.key")
    context.verify_mode = ssl.CERT_OPTIONAL  # clients need not send certs
    context.load_verify_locations(cafile="ca.crt")

    return context


def create_tls_socket(ssl_context, client_socket):
    return ssl_context.wrap_socket(
            client_socket,
            server_side=True
    )


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

    ssl_context = load_ssl_context()

    tcp_socket = create_tcp_socket(server_ip, server_port)
    print(f'Server is running on {server_ip}:{server_port}')

    while True:
        try:
            client_socket, client_address = tcp_socket.accept()
            print(f'New connection from {client_address}')

            s_client_socket = create_tls_socket(ssl_context, client_socket)

            start_client_handler_thread(s_client_socket)

        except KeyboardInterrupt:
            print('\nServer stopped.')
            break

    tcp_socket.close()


if __name__ == "__main__":
    main()
