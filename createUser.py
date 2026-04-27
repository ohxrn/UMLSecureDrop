import json
import os
import pathlib
from helperFuncs import hashPassword

SENSITIVE = "/app/data/secureTable.json"

def createUser():
    print("Let's make you an account! First, enter an email to use for your account: ")
    newEmail = input()
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
        "password": hashPassword(newPassword),
        "friends": [],
        "friendRequests": []
    }

    ####
    os.makedirs("/app/data", exist_ok=True)

    if os.path.isfile(SENSITIVE):
        with open(SENSITIVE, "r") as f:
            table = json.load(f)

        if newEmail not in table:
            table[newEmail] = newAcct
        else:
            print("USER EXISTS ALREADY")
            return -1

        with open(SENSITIVE, "w") as theJSON:
            json.dump(table, theJSON, indent=4)

    else:
        table = {}
        table[newEmail] = newAcct

        with open(SENSITIVE, "w") as theJSON:
            json.dump(table, theJSON, indent=4)

    return newEmail