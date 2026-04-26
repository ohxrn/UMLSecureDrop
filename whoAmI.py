import json
import os
import pathlib
SENSITIVE = "secureTable.json"

def myCreds(credObject):
    with open("myCredentials.json", "w") as f:
        
    # credObject["email"]