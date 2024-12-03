import requests
from os import chdir, path, getcwd
from subprocess import Popen
from version import version

master_version:str 
# Current working directory
CWD = getcwd()

def check_update() -> int:
    global master_version



    master_version =  requests.get("https://raw.githubusercontent.com/Pasquotcho/TimeTracker/refs/heads/master/version").text.strip()

    if version == master_version:
        print("Version up to date!")
        return 0
    
    else:
        print("Version mismatch!")
        return 1

def start_update():
    Popen(f"{CWD}/installer/installer.exe")
    exit()