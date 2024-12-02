import os

APP_DATA_PATH:str = os.path.join(os.environ['APPDATA'], 'Time Project PYQT')

def save_theme(theme:str) -> None:
    with open(f"{APP_DATA_PATH}/theme.dat", "w") as file:
        file.write(theme)

def load_theme() -> None:
    try:
        with open(f"{APP_DATA_PATH}/theme.dat", "r") as file:
            return file.read()
    except FileNotFoundError:
        return "dark"