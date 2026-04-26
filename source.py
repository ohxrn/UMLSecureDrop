import json
import pathlib
import os
from helperFuncs import doesFileExist
from authenticationMod import authenticate

SENSITIVE = "secureTable.json"

def main():
    try:
        print("Do you have an account? (1) for yes, (2) for no")
        yesNo= input()
        if (yesNo == "1"):
            print("Please enter your email: ")
            email = input()
            print("please enter password: ")
            password = input()
            results = authenticate("secureTable.json", email, password)
            if results==-1:
                print("entries do not exist. Err.")
            elif results == 0:
                print("incorrect password")
            else:
                print("Access granted!")

        

        else:
            print("Let's make you an account! First, enter an email to use for your account: ")
            newEmail=input()
            print("Next, enter a unique username to use for your account.")
            username = input()
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
                    "password": newPassword     
            }
            ####
            if os.path.isfile("secureTable.json"):
                with open("secureTable.json", "r") as f:
                    table = json.load(f)
                if newEmail not in table and username not in table:
                    table[username] = newAcct
                        
                else:
                    print("USER EXISTS ALREADY")
                with open("secureTable.json", "w") as theJSON:
                    json.dump(table, theJSON, indent=4)
            else:
                table = {}
                table[newEmail] = newAcct
                with open("secureTable.json", "w") as theJSON:
                    json.dump(table, theJSON, indent=4)
                
                
            print("Great! We have now registered you for our secure drop system.")
            
            print("View contacts? : (1)=Yes (0)=No")
            yayNay = input()
            if (yayNay):
                print("placeholder")
            
            print("Want to add contacts to transfer data? (1)=Yes (2)=no")
            yayNay=input()
            if (yayNay):
                print("Okay. Begin by entering the the username you would like to add:")
                username = input()



    except KeyboardInterrupt:
        print("Program aborted.")

    finally:
        if (os.path.isfile(SENSITIVE)):
            os.remove(SENSITIVE)
            print("CREDENTIALS REMOVED.")
        else:
            print("file doesnt exist.")


    
def userExists(username):
    if (doesFileExist(SENSITIVE)):
        with open (SENSITIVE):
            print("ski")



main()

    
    







