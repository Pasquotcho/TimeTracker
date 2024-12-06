# from requests import get
# import sys
# from os import chdir, path, getcwd
# from subprocess import Popen
# from version import version

# # Current working directory
# CWD = getcwd()

# def check_update() -> int:

#     # Get latest Version
#     request:str =  get("https://api.github.com/repos/Pasquotcho/TimeTracker/releases/latest")
#     data:dict = request.json()
#     master_version:str = data["tag_name"]

#     if version == master_version:
#         print("Version up to date!")
#         return 0
    
#     else:
#         print("Version mismatch!")
#         return 1

# def start_update():
#     Popen("../../installer.exe")
#     sys.exit()