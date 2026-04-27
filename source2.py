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
from authenticationMod import login
from helperFuncs import retrieveHosts
from addRequest import addReq
from addRequest import checkReq
from addRequest import newFriend
ME = "whoami.json"
# CRED="jackohrn1@gmail.com"
SENSITIVE = "/app/data/secureTable.json"

def findOnline(email):
    online = {}
    for host in retrieveHosts():
        response = sendMessage(host, "WHO|" + email)
        if response.startswith("HERE|"):
            other_email = response.split("|")[1]
            if other_email != email:
                online[other_email] = host
    return online


def main():
    myCreds = -1
    authEmail = -1
    #docker setup initially
    os.makedirs("/app/data", exist_ok = True)
     #main while
    #  while (doesFileExist(ME)):
        #initiate multithread
    print("new user? (1)=y (0)=n")
    res = input()
    if (res !="1"):
        myCreds = login()
        if (myCreds!=-1):
            print("welcome, ",myCreds,"!")
           
        else:
            print("error logging in...")
            return
    else:
        myCreds = createUser()
        if (myCreds!=-1):
            print("Loggin in! as:", myCreds)
        else:
            print("could not create user. try again later.")
            return

    threading.Thread(target=initiateBackend,args=(myCreds,),daemon=True
    ).start()
  
    command=1
    while (command!=-1):
        print("secure_drop>")
        print("-Add \n-List\n-Send\n-Req\n-Exit")
        command = input()
        match (command):
            case "Add":
                online = findOnline(myCreds)
                print("friends currently online:")
                for email in online:
                    print(email)
                print("enter email you'd like to add:")
                emailName = input()
                if emailName in online:
                    resi = online[emailName]
                    response = sendMessage(resi, "FR|" + myCreds)
                    print(response)
                else:
                    print("selected user not online.")
    
            case "List":
                printContacts(myCreds)
            case "Send":
                break
            case "Req":
                res = checkReq(myCreds)
                print (res)
                print(f"Accept request from {res} ? (1)=y (0)=n")
                ans = input()
                if (ans =="1"):
                    newFriend(myCreds, res)

                    online = findOnline(myCreds)
                   
                    if res in online:
                        host = online[res]
                        response = sendMessage(host, "MERGEFRIENDS|" + myCreds)
                        print(response)
                    else:
                        print("selected user not online. try again later.")
                else:
                    print("tough")


            case "Exit":
                break
        #grab ur email credentials
    results = sendMessage("alice", "here's my message")
    if (results):
        print("yay")
        
        ########
main()
    





