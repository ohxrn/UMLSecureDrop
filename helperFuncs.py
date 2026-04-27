import os
import pathlib
import json
from cryptography.hazmat.primitives import hashes

SENSITIVE = "/app/data/secureTable.json"

def doesFileExist(file):
    if (os.path.isfile(file)):
        return 1
    else:
        return 0
    
def printContacts(email):
    #temporary hardcode
    if (doesFileExist(SENSITIVE)):
        with open(SENSITIVE, "r") as f:
            data = json.load(f)
            if email in data:
                friends = data[email]["friends"]
                if len(friends)==0:
                    print("No friends added yet!")
                else:
                    print("Your contacts:")
                    for friend in friends:
                        print(friend)
            else:
                print("user not found")
    else: 
        print("secureTable.json does not exist.")
    
def hashPassword(pw):
    digest = hashes.Hash(hashes.SHA256())
    digest.update(pw.encode())
    hashed = digest.finalize()

    return hashed.hex()


def retrieveHosts():
    with open(SENSITIVE, "r") as f:
        data = json.load(f)
    obj = data.get("knownHosts", [])
    return obj