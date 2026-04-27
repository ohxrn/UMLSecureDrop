import json
import pathlib
import threading
import os
from servers.serverSide import initiateBackend
from servers.theClientSide import sendMessage
from helperFuncs import doesFileExist
ME = "whoami.json"

def main(void):
     #docker setup initially
     os.makedirs("/app/data", exist_ok = True)
     #main while
     while (doesFileExist(ME)):
        #initiate multithread
        threading.Thread(target=initiateBackend, daemon=True).start()
        #grab ur email credentials
        





        ########

        break

     

