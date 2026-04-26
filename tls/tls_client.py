import socket
import ssl


def create_tls_socket(server_ip, server_port):
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_socket.connect((server_ip, server_port))

    # wrap socket with ssl
    ssl_context = ssl.create_default_context(
            ssl.Purpose.SERVER_AUTH,
            cafile="ca.crt"
    )
    return ssl_context.wrap_socket(tcp_socket, server_hostname='server')


server_ip = '127.0.0.1'
server_port = 9999

data = input("Enter a message: ").encode('utf-8')

s_tcp_socket = create_tls_socket(server_ip, server_port)

s_tcp_socket.send(data)

data = s_tcp_socket.recv(1024)
print(f"Received from server: {data}")

s_tcp_socket.close()
