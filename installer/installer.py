import win32com.client
from requests import get
from zipfile import ZipFile
from os import environ, path, remove, rename, chdir
from sys import exit
from subprocess import Popen


def update() -> None:

    APP_DATA_PATH:str = path.join(environ['APPDATA'], 'Time Project PYQT')
    FINISHED_PATH:str = path.join(environ['APPDATA'], 'Time Project PYQT', "Distribution", "Time_Tracker.dist")

    # Get latest Version
    request:str =  get("https://api.github.com/repos/Pasquotcho/TimeTracker/releases/latest")
    data:dict = request.json()
    master_version:str = data["tag_name"]
    
    print("Downloading...")
    nf = get(f"https://github.com/Pasquotcho/TimeTracker/releases/download/{master_version}/Time_Tracker.dist.zip")
    print("Downloaded!")

    with open ("dist.zip", "wb") as file:
        file.write(nf.content)

        with ZipFile("dist.zip", "r") as zip_reference:
            print("Extracting...")
            zip_reference.extractall(f"{APP_DATA_PATH}/Distribution")
            print("Extracted!")

    remove("dist.zip")
    if path.exists(f"{FINISHED_PATH}/Time Tracker.exe"):
        remove(f"{FINISHED_PATH}/Time Tracker.exe")
    rename(f"{FINISHED_PATH}/main.exe", f"{FINISHED_PATH}/Time Tracker.exe")
    # opens app in background
    Popen([f"{FINISHED_PATH}/Time Tracker.exe"])

    # Shortcut
    desktop_path = path.join(environ["USERPROFILE"], "Desktop")
    shell = win32com.client.Dispatch("WScript.Shell")

    shortcut = shell.CreateShortcut(f"{desktop_path}/Time Tracker.lnk")
    shortcut.TargetPath = f"{FINISHED_PATH}/Time Tracker.exe"
    shortcut.WorkingDirectory = FINISHED_PATH
    shortcut.save()

    print("Installed")



if __name__=="__main__":
    update()
    exit()