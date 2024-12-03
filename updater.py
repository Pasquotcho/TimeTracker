import requests
import os
from subprocess import Popen
from sys import exit
import zipfile 

master_version:str 
APP_DATA_PATH:str = os.path.join(os.environ['APPDATA'], 'Time Project PYQT')
FINISHED_PATH:str = os.path.join(os.environ['APPDATA'], 'Time Project PYQT', "Distribution", "Time_Tracker")

def check_update() -> int:
    global master_version

    with open ("./version", "r") as file:
        own_version:str = file.readline().strip()

    master_version =  requests.get("https://raw.githubusercontent.com/Pasquotcho/TimeTracker/refs/heads/master/version").text.strip()

    if own_version == master_version:
        print("Version up to date!")
        return 0
    
    else:
        print("Version mismatch!")
        return 1

def update():

    print("Downloading...")
    newfile = requests.get(f"https://github.com/Pasquotcho/TimeTracker/releases/download/{master_version}/Time_Tracker.zip")
    print("Downloaded!")

    with open ("dist.zip", "wb") as file:
        file.write(newfile.content)

        with zipfile.ZipFile("dist.zip", "r") as zip_reference:
            print("Extracting...")
            zip_reference.extractall(f"{APP_DATA_PATH}/Distribution")
            print("Extracted!")

    os.remove("dist.zip")

    # opens app in background
    Popen([f"{FINISHED_PATH}/Time Tracker.exe"])

    # sys exit
    exit()

 
    print("Updated!")
    return 0