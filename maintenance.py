import os
import lib
import var
from screen import log
try:
    import requests
except:
    print("Unable to load requests module ...")
    exit()

def check():
    if int(lib.read_file_config(var.REGISTERY().main_file_config_path, "[AUTOMAINTENANCE]")):
        try:
            if list(requests.get("https://www.projet-voltaire.fr/").text.split("maintenance")[0].replace(" ", ""))[-1] == 'n':
                return True
            else:
                return False
        except:
            return False
    else:
        log("Cancelling maintenance checking ...")