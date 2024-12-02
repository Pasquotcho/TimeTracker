style_dict = {
"dark": '''
    QWidget {
        background-color: #121212;
        color: #e5e5e5;
        font-family: 'Roboto', sans-serif;
    }

    QLabel {
        font-size: 20px;
        margin-bottom: 12px;
        color: #e5e5e5;
    }

    QTimeEdit {
        text-align: center;
        background-color: #2d2d2d;
        color: #e5e5e5;
        border: 2px solid #444444;
        border-radius: 10px;
        padding: 14px;
        min-width: 250px;
        min-height: 50px;
        font-size: 20px;
    }

    QPushButton {
        background-color: #1f80e0;
        color: #ffffff;
        border: none;
        border-radius: 12px;
        padding: 12px;
        font-size: 18px;
    }

    QPushButton:hover {
        background-color: #1676c2;
    }

    QPushButton:pressed {
        background-color: #156fa1; /* Etwas dunklerer Button, wenn gedrückt */
    }

    QPushButton:disabled {
        background-color: #4b5561;
        color: #bcc4d1;
    }

    QLabel#how_long {
        font-size: 16px;
        font-weight: bold;
        margin-top: 15px;
    }

    QLabel#explanation {
        border: 2px solid #444444;
        border-radius: 10px;
        padding: 15px;
        background-color: #333333;
        color: #e5e5e5;
        font-size: 16px;
    }

    QProgressBar {
        background-color: #2d2d2d;
        border: 1px solid #444444;
        border-radius: 10px;
        text-align: center;
        color: #e5e5e5;
        font-size: 16px;
        height: 25px;
    }

    QProgressBar::chunk {
        background-color: #00c0ff;
        border-radius: 6px;
    }

    QCheckBox {
        color: #e5e5e5;
        font-size: 18px;
        padding-left: 10px;
    }

    QCheckBox::indicator {
        width: 22px;
        height: 22px;
    }

    QCheckBox::indicator:unchecked {
        background-color: #2d2d2d;
        border: 2px solid #444444;
        border-radius: 4px;
    }

    QCheckBox::indicator:checked {
        background-color: #00c0ff;
        border: 2px solid #444444;
        border-radius: 4px;
    }

    QCheckBox::indicator:checked:focus {
        border: 2px solid #ffffff;
    }
    ''',
"light": '''
    QWidget {
        background-color: #f0f4f8;
        color: #2b3a42;
        font-family: 'Arial', sans-serif;
    }

    QLabel {
        font-size: 20px;
        margin-bottom: 12px;
        color: #2b3a42;
    }

    QTimeEdit {
        text-align: center;
        background-color: #dfe7ef;
        color: #2b3a42;
        border: 2px solid #a0b1c4;
        border-radius: 10px;
        padding: 14px;
        min-width: 250px;
        min-height: 50px;
        font-size: 20px;
    }

    QPushButton {
        background-color: #ff7e47;
        color: #ffffff;
        border: none;
        border-radius: 12px;
        padding: 12px;
        font-size: 18px;
    }

    QPushButton:hover {
        background-color: #e9703b;
    }

    QPushButton:pressed {
        background-color: #d86533;
    }

    QPushButton:disabled {
        background-color: #b0b8bf;
        color: #e0e6eb;
    }

    QLabel#how_long {
        font-size: 16px;
        font-weight: bold;
        margin-top: 15px;
    }

    QLabel#explanation {
        border: 2px solid #a0b1c4;
        border-radius: 10px;
        padding: 15px;
        background-color: #e7eff5;
        color: #2b3a42;
        font-size: 16px;
    }

    QProgressBar {
        background-color: #dfe7ef;
        border: 1px solid #a0b1c4;
        border-radius: 10px;
        text-align: center;
        color: #2b3a42;
        font-size: 16px;
        height: 25px;
    }

    QProgressBar::chunk {
        background-color: #ff7e47;
        border-radius: 6px;
    }

    QCheckBox {
        color: #2b3a42;
        font-size: 18px;
        padding-left: 10px;
    }

    QCheckBox::indicator {
        width: 22px;
        height: 22px;
    }

    QCheckBox::indicator:unchecked {
        background-color: #dfe7ef;
        border: 2px solid #a0b1c4;
        border-radius: 4px;
    }

    QCheckBox::indicator:checked {
        background-color: #ff7e47;
        border: 2px solid #a0b1c4;
        border-radius: 4px;
    }

    QCheckBox::indicator:checked:focus {
        border: 2px solid #2b3a42;
    }
    ''',
"girly": '''
    QWidget {
        background-color: #f8e1f4;
        color: #7b2e88;
        font-family: 'Comic Sans MS', sans-serif;
    }

    QLabel {
        font-size: 22px;
        margin-bottom: 12px;
        color: #7b2e88;
    }

    QTimeEdit {
        text-align: center;
        background-color: #ffd4e5;
        color: #7b2e88;
        border: 2px solid #f1b1e0;
        border-radius: 10px;
        padding: 14px;
        min-width: 250px;
        min-height: 50px;
        font-size: 20px;
    }

    QPushButton {
        background-color: #ff80df;
        color: #ffffff;
        border: none;
        border-radius: 12px;
        padding: 12px;
        font-size: 18px;
    }

    QPushButton:hover {
        background-color: #ff63c8;
    }

    QPushButton:pressed {
        background-color: #e856ad;
    }

    QPushButton:disabled {
        background-color: #f1c8d3;
        color: #e7a2bc;
    }

    QLabel#how_long {
        font-size: 18px;
        font-weight: bold;
        margin-top: 15px;
    }

    QLabel#explanation {
        border: 2px solid #f1b1e0;
        border-radius: 10px;
        padding: 15px;
        background-color: #fef3f7;
        color: #7b2e88;
        font-size: 16px;
    }

    QProgressBar {
        background-color: #ffd4e5;
        border: 1px solid #f1b1e0;
        border-radius: 10px;
        text-align: center;
        color: #7b2e88;
        font-size: 16px;
        height: 25px;
    }

    QProgressBar::chunk {
        background-color: #ff80df;
        border-radius: 6px;
    }

    QCheckBox {
        color: #7b2e88;
        font-size: 18px;
        padding-left: 10px;
    }

    QCheckBox::indicator {
        width: 22px;
        height: 22px;
    }

    QCheckBox::indicator:unchecked {
        background-color: #ffd4e5;
        border: 2px solid #f1b1e0;
        border-radius: 4px;
    }

    QCheckBox::indicator:checked {
        background-color: #ff80df;
        border: 2px solid #f1b1e0;
        border-radius: 4px;
    }

    QCheckBox::indicator:checked:focus {
        border: 2px solid #7b2e88;
    }
    ''',
"evil": '''
    QWidget {
        background-color: #1c1c1c;
        color: #e10000;
        font-family: 'Impact', sans-serif;
    }

    QLabel {
        font-size: 24px;
        margin-bottom: 12px;
        color: #e10000;
    }

    QTimeEdit {
        text-align: center;
        background-color: #333333;
        color: #e10000;
        border: 2px solid #d40000;
        border-radius: 10px;
        padding: 14px;
        min-width: 250px;
        min-height: 50px;
        font-size: 20px;
    }

    QPushButton {
        background-color: #900000;
        color: #ffffff;
        border: none;
        border-radius: 12px;
        padding: 12px;
        font-size: 18px;
    }

    QPushButton:hover {
        background-color: #750000;
    }

    QPushButton:pressed {
        background-color: #5c0000;
    }

    QPushButton:disabled {
        background-color: #4b4b4b;
        color: #8e8e8e;
    }

    QLabel#how_long {
        font-size: 18px;
        font-weight: bold;
        margin-top: 15px;
    }

    QLabel#explanation {
        border: 2px solid #d40000;
        border-radius: 10px;
        padding: 15px;
        background-color: #222222;
        color: #e10000;
        font-size: 16px;
    }

    QProgressBar {
        background-color: #333333;
        border: 1px solid #d40000;
        border-radius: 10px;
        text-align: center;
        color: #e10000;
        font-size: 16px;
        height: 25px;
    }

    QProgressBar::chunk {
        background-color: #900000;
        border-radius: 6px;
    }

    QCheckBox {
        color: #e10000;
        font-size: 18px;
        padding-left: 10px;
    }

    QCheckBox::indicator {
        width: 22px;
        height: 22px;
    }

    QCheckBox::indicator:unchecked {
        background-color: #333333;
        border: 2px solid #d40000;
        border-radius: 4px;
    }

    QCheckBox::indicator:checked {
        background-color: #900000;
        border: 2px solid #d40000;
        border-radius: 4px;
    }

    QCheckBox::indicator:checked:focus {
        border: 2px solid #ffffff;
    }
    ''',
"childish_blue": '''
    QWidget {
        background-color: #e8faff;
        color: #007bff;
        font-family: 'Verdana', sans-serif;
    }

    QLabel {
        font-size: 22px;
        margin-bottom: 12px;
        color: #007bff;
    }

    QTimeEdit {
        text-align: center;
        background-color: #d9f4ff;
        color: #007bff;
        border: 2px solid #00c1ff;
        border-radius: 10px;
        padding: 14px;
        min-width: 250px;
        min-height: 50px;
        font-size: 20px;
    }

    QPushButton {
        background-color: #00c1ff;
        color: #ffffff;
        border: none;
        border-radius: 12px;
        padding: 12px;
        font-size: 18px;
    }

    QPushButton:hover {
        background-color: #00a1e0;
    }

    QPushButton:pressed {
        background-color: #0081c0;
    }

    QPushButton:disabled {
        background-color: #a0d7f0;
        color: #d0f2ff;
    }

    QLabel#how_long {
        font-size: 18px;
        font-weight: bold;
        margin-top: 15px;
    }

    QLabel#explanation {
        border: 2px solid #00c1ff;
        border-radius: 10px;
        padding: 15px;
        background-color: #ccf4ff;
        color: #007bff;
        font-size: 16px;
    }

    QProgressBar {
        background-color: #d9f4ff;
        border: 1px solid #00c1ff;
        border-radius: 10px;
        text-align: center;
        color: #007bff;
        font-size: 16px;
        height: 25px;
    }

    QProgressBar::chunk {
        background-color: #007bff;
        border-radius: 6px;
    }

    QCheckBox {
        color: #007bff;
        font-size: 18px;
        padding-left: 10px;
    }

    QCheckBox::indicator {
        width: 22px;
        height: 22px;
    }

    QCheckBox::indicator:unchecked {
        background-color: #d9f4ff;
        border: 2px solid #00c1ff;
        border-radius: 4px;
    }

    QCheckBox::indicator:checked {
        background-color: #007bff;
        border: 2px solid #00c1ff;
        border-radius: 4px;
    }

    QCheckBox::indicator:checked:focus {
        border: 2px solid #ffffff;
    }
    '''


}

def apply_styles(app: object, style:str = "dark"):
    global style_dict
    app.setStyleSheet(style_dict[style])
