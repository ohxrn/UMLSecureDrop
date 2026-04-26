import os
import pathlib
def doesFileExist(file):
    if (os.path.isfile(file)):
        return 1
    else:
        return 0