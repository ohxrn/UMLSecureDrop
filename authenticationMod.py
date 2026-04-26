import os
import pathlib
import json
from helperFuncs import doesFileExist

def authenticate(accounts, acctU, acctP):
    if doesFileExist(accounts):
        with open(accounts, "r") as f:
            data = json.load(f)
            if acctU in data:
                if data[acctU]["password"]==acctP:
                    return 1
                else:
                    return 0
    return -1