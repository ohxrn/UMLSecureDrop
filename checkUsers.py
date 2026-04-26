from helperFuncs import doesFileExist 
import json

SENSITIVE = "/app/data/secureTable.json"
def userExists(username):
    if (doesFileExist(SENSITIVE)):
        with open (SENSITIVE, "r") as f:
            data = json.load(f)
            if username in data:
                return 1
            else:
                return 0