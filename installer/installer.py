from requests import get
from zipfile import ZipFile
from os import environ, path, remove
from sys import exit
from subprocess import Popen

def update() -> None:

    APP_DATA_PATH:str = path.join(environ['APPDATA'], 'Time Project PYQT')
    FINISHED_PATH:str = path.join(environ['APPDATA'], 'Time Project PYQT', "Distribution", "Time_Tracker")

    master_version =  get("https://raw.githubusercontent.com/Pasquotcho/TimeTracker/refs/heads/master/version").text.strip()

    print("Downloading...")
    newfile = get(f"https://github.com/Pasquotcho/TimeTracker/releases/download/{master_version}/Time_Tracker.dist.zip")
    print("Downloaded!")

    with open ("dist.zip", "wb") as file:
        file.write(newfile.content)

        with ZipFile("dist.zip", "r") as zip_reference:
            print("Extracting...")
            zip_reference.extractall(f"{APP_DATA_PATH}/Distribution")
            print("Extracted!")

    remove("dist.zip")

    # opens app in background
    Popen([f"{FINISHED_PATH}/Time Tracker.exe"])

    # sys exit
    exit()

    print("Updated!")

if __name__=="__main__":
    update()
    exit()