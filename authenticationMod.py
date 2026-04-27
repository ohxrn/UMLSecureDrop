import os
import pathlib
import json
from helperFuncs import doesFileExist
from helperFuncs import hashPassword

SENSITIVE = "/app/data/secureTable.json"

def authenticate(accounts, acctU, acctP):
    if doesFileExist(accounts):
        with open(accounts, "r") as f:
            data = json.load(f)
            if acctU in data:
                if data[acctU]["password"]==hashPassword(acctP):
                    return 1
                else:
                    return 0
    return -1

def login():
    print("enter email:")
    nE = input()
    print("enter password:")
    nP = input()
    results = authenticate(SENSITIVE, nE, nP)
    if (results==1):
        print("yay ur real")
    else:
        trigger = 0
        inc=0
        while(trigger!=1):
            if (inc>2):
                print("too many attempts. Try again later.")
                return -1
            print("not correct combo. Try again.")
            print("enter email:")
            nE = input()
            print("enter password:")
            nP = input()
            trigger = authenticate(SENSITIVE, nE, nP)
            inc+=1
    return nE