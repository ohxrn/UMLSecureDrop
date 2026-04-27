import socket
import ssl
from pathlib import Path
import os
OFFICIAL_CA = "/app/docker_content/tls/ca.crt"
def sendMessage(host, message):
    raw_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        raw_socket.connect((host, 9999))

        context = ssl.create_default_context(
        ssl.Purpose.SERVER_AUTH,
        cafile=OFFICIAL_CA
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
    
def sendFile(host, sEmail, filepath):
    filename = os.path.basename(filepath)
    raw_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    raw_socket.connect((host, 9999))

    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile=OFFICIAL_CA)
    context.check_hostname = False
    context.verify_mode = ssl.CERT_REQUIRED
    tls_socket = context.wrap_socket(raw_socket)
    tls_socket.send(("FILE|" + sEmail + "|" + filename).encode())
    response = tls_socket.recv(1024).decode()

    if (response != "ACCEPT"):
        print("Rejected")
        tls_socket.close()
        return 0
    with open(filepath, "rb") as f:
        while True:
            bits = f.read(4096)
            if not bits:
                break
            tls_socket.send(bits)
    tls_socket.close()
    print("FILE WAS SENT")
    return 1

