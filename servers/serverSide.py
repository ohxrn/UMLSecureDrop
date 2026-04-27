import socket
import ssl
from pathlib import Path


TLS_DIR = Path(__file__).resolve().parent.parent / "docker_content" / "tls"

def initiateBackend():
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(
        certfile=str(TLS_DIR / "server.pem"),
        keyfile=str(TLS_DIR / "server.key")
    )

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 9999))
    server.listen(5)

    # print("-----------TLS listener now active------------")

    while True:
        try:
            client_socket, client_address = server.accept()

            tls_socket = context.wrap_socket(client_socket, server_side=True)

            print(client_address, "joined securely")

            data = tls_socket.recv(1024)
            print("Message:", data.decode())

            tls_socket.send("TLS RECEIVED".encode())
            tls_socket.close()

        except KeyboardInterrupt:
            server.close()
            print("stopped")
            break