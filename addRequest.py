import json
from helperFuncs import doesFileExist

SENSITIVE = "/app/data/secureTable.json"

def addReq(credObj, email):
    if (doesFileExist(SENSITIVE)):
        with open (SENSITIVE, "r") as f:
            data = json.load(f)
        if email in data:
            data[email]["friendRequests"].append(credObj)
            with open(SENSITIVE, "w") as reSync:
                json.dump(data, reSync, indent=4)
                print("successfully added.")
                return 1
        else:
            print("never found email.")
            return 0

def checkReq(credE):
    if (doesFileExist(SENSITIVE)):
        with open (SENSITIVE, "r") as f:
            data = json.load(f)
        if credE in data:
            requestList = data[credE]["friendRequests"]
            inc=0
            for friendRequests in requestList:
                print(friendRequests)
                inc+=1
            print("AMT OF REQUESTS: " , inc)


            with open(SENSITIVE, "w") as reSync:
                json.dump(data, reSync, indent=4)
                print("successfully added.")
                return 1
        else:
            print("never found email.")
            return 0



   

