import json
import pathlib
import threading
import os
from servers.serverSide import initiateBackend
from servers.theClientSide import sendMessage
from helperFuncs import doesFileExist
from helperFuncs import printContacts
from authenticationMod import authenticate
from createUser import createUser
ME = "whoami.json"
CRED="jackohrn1@gmail.com"
SENSITIVE = "/app/data/secureTable.json"

def main():
    #docker setup initially
    os.makedirs("/app/data", exist_ok = True)
     #main while
    #  while (doesFileExist(ME)):
        #initiate multithread
    threading.Thread(target=initiateBackend, daemon=True).start()
    print("new user? (1)=y (0)=n")
    res = input()
    if (res==0):
        print("enter email:")
        nE = input()
        print("enter password:")
        nP = input()
        results = authenticate(SENSITIVE, nE, nP)
        if (results):
            print("yay ur real")
        else:
            print("not correct combo.")


    myCreds = createUser()
    if (myCreds!=-1):
        print("Loggin in! as:", myCreds)



    command=1
    while (command!=-1):
        print("secure_drop>")
        print("-Add \n-List\n-Send\n-Exit")
        command = input()
        match (command):
            case "Add":
                print("enter email you'd like to add:")
                emailName = input()
                break
            case "List":
                printContacts("jackohrn1@gmail.com")
            case "Send":
                break
            case "Exit":
                break
        #grab ur email credentials
    results = sendMessage("alice", "here's my message")
    if (results):
        print("yay")
        





        ########
main()
      