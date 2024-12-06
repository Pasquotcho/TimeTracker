import json
import os
from PySide6 import QtCore, QtWidgets
from random import choice
from styles import apply_styles
from theme_handler import load_theme, save_theme
from updater import check_update, start_update

APP_DATA_PATH:str = os.path.join(os.environ['APPDATA'], 'Time Project PYQT')
ALL_STYLES = ["dark", "girly", "light", "evil", "childish_blue"]

class TimeCounterApp(QtWidgets.QWidget):
    
    def __init__(self) -> None:
        super().__init__() 
        self.timer:QtCore.QTimer = QtCore.QTimer(self) #Self übergeben um Speicherlecks zu vermeiden
        
        self.expected_time:QtCore.QTime = None
        self.arrived_time:QtCore.QTime = None
        self.time_till_home:int = None
        self.theme:str = load_theme()
       
        self.label_for_time_input:QtWidgets.QLabel = QtWidgets.QLabel("Wann bist du Heute in der Arbeit angekommen?")
        self.time_input:QtWidgets.QTimeEdit = QtWidgets.QTimeEdit()
        self.time_input.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons) #Keine Buttons im Time Edit
        self.send_button:QtWidgets.QPushButton = QtWidgets.QPushButton("Abfragen")
        self.check_friday:QtWidgets.QCheckBox = QtWidgets.QCheckBox("Sechs Stunden Tag!")
        
        self.progressbar:QtWidgets.QProgressBar = QtWidgets.QProgressBar()
        self.progressbar.setRange(-510, 0) #8,5h in sekunden 
        self.progressbar.hide()

        self.explanation:QtWidgets.QLabel = QtWidgets.QLabel()
        self.explanation.setObjectName("explanation")
        self.how_long:QtWidgets.QLabel = QtWidgets.QLabel()
        self.update_button:QtWidgets.QPushButton = QtWidgets.QPushButton("Update Verfügbar!")
        self.update_button.setObjectName("update_btn")
        self.update_button.setProperty("class", "exclude")

        self.send_button.clicked.connect(self.time_changed)
        self.timer.timeout.connect(self.home_timer)
        
        align_center:QtCore.Qt = QtCore.Qt.AlignCenter
        align_right:QtCore.Qt = QtCore.Qt.AlignRight

        self.layout:QtWidgets.QVBoxLayout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.progressbar)
        self.layout.addWidget(self.label_for_time_input, alignment=align_center)
        self.layout.addWidget(self.time_input, alignment=align_center)
        self.layout.addWidget(self.check_friday, alignment=align_center)
        self.layout.addWidget(self.send_button)

        self.layout.addWidget(self.explanation, alignment=align_center)
        self.explanation.hide()

        self.layout.addWidget(self.how_long, alignment=align_center)

        ## Update
        if check_update() == 1:
            self.layout.addWidget(self.update_button, alignment=align_right)

        self.switch_theme:QtWidgets.QPushButton = QtWidgets.QPushButton("Style Ändern")

        self.theme_1: QtWidgets.QPushButton = QtWidgets.QPushButton("Dark")
        self.theme_1.setObjectName("dark")
        self.theme_1.hide()

        self.theme_2: QtWidgets.QPushButton = QtWidgets.QPushButton("Light")
        self.theme_2.setObjectName("light")
        self.theme_2.hide()

        self.theme_3: QtWidgets.QPushButton = QtWidgets.QPushButton("Girly")
        self.theme_3.setObjectName("girly")
        self.theme_3.hide()

        self.theme_4: QtWidgets.QPushButton = QtWidgets.QPushButton("Evil")
        self.theme_4.setObjectName("evil")
        self.theme_4.hide()

        self.theme_5: QtWidgets.QPushButton = QtWidgets.QPushButton("Childish")
        self.theme_5.setObjectName("childish_blue")
        self.theme_5.hide()

        self.theme_button_layout:QtWidgets.QHBoxLayout = QtWidgets.QHBoxLayout()
        self.layout.addLayout(self.theme_button_layout)

        self.theme_button_layout.addWidget(self.theme_1)
        self.theme_1.clicked.connect(lambda: self.change_theme(self.theme_1.objectName()))
        self.theme_button_layout.addWidget(self.theme_2)
        self.theme_2.clicked.connect(lambda: self.change_theme(self.theme_2.objectName()))
        self.theme_button_layout.addWidget(self.theme_3)
        self.theme_3.clicked.connect(lambda: self.change_theme(self.theme_3.objectName()))
        self.theme_button_layout.addWidget(self.theme_4)
        self.theme_4.clicked.connect(lambda: self.change_theme(self.theme_4.objectName()))
        self.theme_button_layout.addWidget(self.theme_5)
        self.theme_5.clicked.connect(lambda: self.change_theme(self.theme_5.objectName()))


        self.theme_button_layout.addWidget(self.switch_theme, alignment=align_right)

        self.switch_theme.clicked.connect(self.theme_button_clicked)
        
        #Update Button 
        self.update_button.clicked.connect(self.update)
     
        if not self.load_data() == 2:
            self.time_changed()

    def time_changed(self) -> None:

        if self.check_friday.isChecked():
            self.progressbar.setRange(-360, 0)
            self.expected_time:QtCore.QTime = self.time_input.time().addSecs(6 * 3600) # ADD 6H in Seconds
            self.arrived_time:QtCore.QTime = self.time_input.time()
        else:
            self.progressbar.setRange(-510, 0)
            self.expected_time:QtCore.QTime = self.time_input.time().addSecs(8 * 3600 + 30 * 60) # ADD 8H 30M in Seconds
            self.arrived_time:QtCore.QTime = self.time_input.time()

        self.explanation.setText("")
        self.save_data()
        self.save_log()
        self.load_data()

        text:str = f"Ankunft: {self.time_input.time().toString("HH:mm")} Gehen: {self.expected_time.toString("HH:mm")}"
        self.explanation.setText(text)
    
    def load_data(self) -> int|None:
        os.makedirs(APP_DATA_PATH, exist_ok=True)

        current_date:int = QtCore.QDateTime.currentDateTime().date().day()
        if "Fri" in QtCore.QDateTime.currentDateTime().toString(): #If Day is Friday
            self.check_friday.setChecked(True)

        if not os.path.exists(f"{APP_DATA_PATH}/time_protocoll.json"):
            with open(f"{APP_DATA_PATH}/time_protocoll.json", "w") as file:
                return 2
        else:
            with open(f"{APP_DATA_PATH}/time_protocoll.json", "r") as file:

                try:
                    data:dict = json.load(file)
                except json.JSONDecodeError:
                    return 1

                logtime:QtCore.QDateTime = QtCore.QDateTime.fromString(data["logtime"])
                
                
                if current_date != logtime.date().day(): #If last log day not Yesterday. Show no Time 
                    return 2

                arrived:QtCore.QTime = QtCore.QTime.fromString(data["arrived"])
                expected:QtCore.QTime = QtCore.QTime.fromString(data["expected"])
                if arrived != "" and expected != "":
                    self.explanation.show()
                    self.progressbar.setValue(-510)
                    self.progressbar.show()

                self.expected_time:QtCore.QTime = expected
                self.arrived_time:QtCore.QTime = arrived

                text:str = f"Ankunft: {arrived.toString("HH:mm")} Gehen: {expected.toString("HH:mm")}"

                self.explanation.setText(text)
                self.time_input.setTime(arrived)
                
                self.home_timer()
                self.timer.start(1000)  # 1 Sec Timer
                self.change_theme(load_theme())


    def save_data(self) -> None:

        with open(f"{APP_DATA_PATH}/time_protocoll.json", "w") as file:

            data:dict = {
                "logtime": QtCore.QDateTime.currentDateTime().toString(),
                "arrived": self.arrived_time.toString(),
                "expected": self.expected_time.toString()
                }
            
            json.dump(data, file, indent=4)

            save_theme(self.theme)


    def save_log(self) -> None:

        with open(f"{APP_DATA_PATH}/time_protocoll.txt", "a") as file:
            file.write(f"[{QtCore.QDateTime.currentDateTime().toString()}] -- Arrived: {self.arrived_time.toString()} Expected: {self.expected_time.toString()}\n")
    

    def difference_calculator(self) -> None:
       
        current_time:QtCore.QTime = QtCore.QTime.currentTime()
        self.time_till_home:int = current_time.secsTo(self.expected_time)
        
        # Progressbar
        self.progressbar.setValue(-(self.time_till_home / 60) - 1)


    def home_timer(self) -> None:

        self.difference_calculator()
        self.time_till_home *= 1000 #Seconds to Miliseconds
        time:QtCore.QTime = QtCore.QTime.fromMSecsSinceStartOfDay(abs(self.time_till_home))

        if self.time_till_home <= 0:
            self.progressbar.setValue(0)
            self.how_long.setText(f"Du bist schon {time.toString()} zu lange hier.")
        else:
            self.how_long.setText(f"Das ist in {time.toString()}")
        
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Enter or event.key() == QtCore.Qt.Key_Return:
            self.send_button.click()
        else:
            return super().keyPressEvent(event)
    
    def change_theme(self, theme:str) -> None:
        self.theme = theme
        apply_styles(self, theme)

    def theme_button_clicked(self) -> None:
        
        for i, _ in enumerate(ALL_STYLES, start=1):
            theme:QtWidgets.QPushButton = getattr(self, f"theme_{i}")
            if theme.isHidden():
                theme.show()
                self.switch_theme.setText("Einklappen")
            else:
                theme.hide()
                self.switch_theme.setText("Style Ändern")

    def update(self) -> None:
        self.close()
        start_update()
