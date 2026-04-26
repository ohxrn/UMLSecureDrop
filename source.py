import json
import pathlib
import os

def main():
    print("Do you have an account? (1) for yes, (2) for no")
    yesNo= input()
    if (yesNo == "1"):
        print("Please enter your email: ")
        email = input()
        print("please enter password: ")
        password = input()
        results = authenticate("secureTable.json", email, password)
        
       

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

    
def authenticate(accounts, acctU, acctP):
    
    if (os.path.isfile(accounts)):
        with open(accounts, "r") as f:
            data = json.load(f)
            if acctU in data:
                if data[acctU]["password"]==acctP:
                    return 1
                else:
                    return 0

main()

    
    







