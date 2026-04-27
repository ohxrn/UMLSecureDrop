import socket
import ssl
from pathlib import Path


def sendMessage(host, message):
    raw_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        raw_socket.connect((host, 9999))

        context = ssl.create_default_context(
        ssl.Purpose.SERVER_AUTH,
        cafile="/app/docker_content/tls/ca.crt"
)
        
        context.check_hostname = False
        context.verify_mode = ssl.CERT_REQUIRED

        tls_socket = context.wrap_socket(raw_socket)

        tls_socket.send(message.encode())

        response = tls_socket.recv(1024).decode()
        tls_socket.close()

        return response

    except ConnectionRefusedError:
        return "OFFLINE"

    except socket.gaierror:
        return "HOST_NOT_FOUND"