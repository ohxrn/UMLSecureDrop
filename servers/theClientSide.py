import socket
import threading

print("")
 
def sendMessage(host,message):
    print("starting....")
    
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, 9999))
        client.send(message.encode())

        response = client.recv(1024)
        print("response:", response.decode())
        

    except KeyboardInterrupt:
        client.close()
        print("client stopped.")

    except ConnectionRefusedError:
        print("Server cant accept rn")

    finally:
        client.close()





