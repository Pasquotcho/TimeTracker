from PySide6 import QtWidgets
from widgets import TimeCounterApp
from PySide6.QtGui import QIcon
import styles
from reload_styles import reload_styles
from theme_handler import save_theme, load_theme

if __name__ == "__main__":    
    myapp = QtWidgets.QApplication([])
    window = TimeCounterApp()
    reload_styles()
    styles.apply_styles(window, style=load_theme())
    window.resize(800,600)
    window.show()
    window.setWindowTitle("Time Counter")
    window.setWindowIcon(QIcon(":/assets/1488492634-man07_81748.ico"))
    myapp.exec()
    save_theme(window.theme)
    
