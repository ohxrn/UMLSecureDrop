import socket
def startClientServer(service):
    print("starting....")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((service, 9999))
    client.send("hello main server".encode())
    client.close()




startClientServer("central_service")