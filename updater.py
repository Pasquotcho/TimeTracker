import requests
import os
from subprocess import Popen
from sys import exit
import zipfile 

master_version:str 
# Current working directory
CWD = os.getcwd()
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

def start_update():
    Popen(f"{CWD}/installer/installer.exe")
    exit()