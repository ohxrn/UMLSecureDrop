import socket
import ssl
from pathlib import Path


TLS_DIR = Path(__file__).resolve().parent.parent / "docker_content" / "tls"

def sendMessage(host, message):
    raw_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        raw_socket.connect((host, 9999))

        context = ssl.create_default_context(
            ssl.Purpose.SERVER_AUTH,
            cafile=str(TLS_DIR / "ca.crt")
        )

        tls_socket = context.wrap_socket(raw_socket, server_hostname="server")

        tls_socket.send(message.encode())

        response = tls_socket.recv(1024)
        print("response:", response.decode())

        tls_socket.close()

    except ConnectionRefusedError:
        print("Server cant accept rn")

    except socket.gaierror:
        print("Could not find host:", host)



