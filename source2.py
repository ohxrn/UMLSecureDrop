import json
import pathlib
import threading
import os
from servers.serverSide import initiateBackend
from servers.theClientSide import sendMessage
from helperFuncs import doesFileExist
ME = "/app/data/whoami.json"


def getEmail():
    if (doesFileExist(ME)):
        with open (ME, "r") as f:
            data = json.load(f)
            email=data["email"]
            return email
    else:
        print("file doesnt exist")
    return -1

        
    

def main():
    os.makedirs("/app/data", exist_ok=True)

    if not doesFileExist(ME):
        print("file does not exist")
        return

    threading.Thread(target=initiateBackend, daemon=True).start()

    email = getEmail()

    while True:
        command = input("secure_drop> ")

        if command == "send":
            host = input("Enter host to send to: ")
            sendMessage(host, email)

        elif command == "exit":
            break

        else:
            print("Commands: send, exit")

    
 

main()