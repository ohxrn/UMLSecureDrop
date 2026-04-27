import threading
import json
import pathlib
import os
from helperFuncs import doesFileExist
from authenticationMod import authenticate
from checkUsers import userExists
from addRequest import addReq 
from addRequest import checkReq
from servers.theClientSide import sendMessage
from servers.serverSide import initiateBackend

# from whoAmI import myCreds

SENSITIVE = "/app/data/secureTable.json"
MYCREDENTIALS={}

def main():

    try:
        print("Do you have an account? (1) for yes, (2) for no")
        yesNo= input()
        if (yesNo == "1"):
            print("Please enter your email: ")
            email = input()
            print("please enter password: ")
            password = input()
            results = authenticate(SENSITIVE, email, password)
            if results==-1:
                print("entries do not exist. Err.")
            elif results == 0:
                print("incorrect password")
            else:
                MYCREDENTIALS = {
                    "email":email,
                    "password":password
                }
                print("Access granted!")
                

        

        else:
            print("Let's make you an account! First, enter an email to use for your account: ")
            newEmail=input()
            print("Now enter a good password for you to use: ")
            newPassword = input()
            print("reenter password to verify match: ")
            newP1 = input()

            while (newP1 != newPassword):
                print("Passwords do not match. Please try again.")
                print("enter a good password for you to use: ")
                newPassword = input()
                print("reenter password to verify match: ")
                newP1 = input()
            newAcct = {
                    "email": newEmail,
                    "password": newPassword,
                    "friends":[],
                    "friendRequests":[]     
            }
            MYCREDENTIALS = {
                "email":newEmail,
                "password":newPassword
            }
            ####
            os.makedirs("/app/data", exist_ok = True)
            if os.path.isfile(SENSITIVE):
                with open(SENSITIVE, "r") as f:
                    table = json.load(f)
                if newEmail not in table:
                    table[newEmail] = newAcct
                else:
                    print("USER EXISTS ALREADY")
                with open(SENSITIVE, "w") as theJSON:
                    json.dump(table, theJSON, indent=4)
            else:
                table = {}
                table[newEmail] = newAcct
                with open(SENSITIVE, "w") as theJSON:
                    json.dump(table, theJSON, indent=4)

            threading.Thread(target=initiateBackend, daemon=True).start()
            sendMessage("yo anyone there")
        
            print("Great! We have now registered you for our secure drop system.")

            
        print("View contacts? : (1)=Yes (0)=No")
        yayNay = input()
        if (yayNay):
            print("placeholder")
        print("Want to add contacts to transfer data? (1)=Yes (2)=no")
        yayNay=input()
        if (yayNay):
            print("Okay. Enter the the email you would like to add:")
            username = input()
            res = userExists(username)
            if res == 1:
                print(username+"exists - would you like to connect with this user? (1)=yes, (0)=no")
                isYes = input()
                if (isYes):
                    results = addReq(MYCREDENTIALS["email"], username)
                    print("request sent to " + username)
        ##---------
        print("View friend requests?")
        sure = input()
        if (sure):
            results = checkReq(MYCREDENTIALS["email"])
        else:
            print("womp womp. ending prog now.")
    
                        


            
    except KeyboardInterrupt:
        print("Program aborted.")

    finally:
        if (os.path.isfile(SENSITIVE)):
            # os.remove(SENSITIVE)
            print("CREDENTIALS REMOVED.")
        else:
            print("file doesnt exist.")






main()

    
    







