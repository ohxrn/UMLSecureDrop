import socket
def startClientServer(service):
    print("starting....")
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((service, 9999))
        client.send("BAHAHAHA SKDING".encode())
        

    except KeyboardInterrupt:
        client.close()
        print("client stopped.")

    except ConnectionRefusedError:
        print("Server cant accept rn")

    finally:
        client.close()





startClientServer("central_service")