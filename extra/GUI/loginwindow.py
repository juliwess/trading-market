# This Python file uses the following encoding: utf-8
import sys
import threading
import time
import uvicorn
import os
import json
import requests
import csv
from market import Market
from trader import Trader
from account import Account
from good import Good
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Slot


# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic login.ui -o ui_loginwindow.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_login import Ui_LoginWindow


def update():
    while(True):
        requests.get("http://localhost:8000/refresh-values")
        time.sleep(5)



class LoginWindow(QWidget):
    def __init__(self, parent=None):
        #setup the ui
        super().__init__(parent)
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)

        #declare password and id
        self.ID: int = None
        self.password: str = None

        #connecdt lineEdits to their corresponding slot functions
        self.ui.lineEditID.textChanged.connect(self.updateID)
        self.ui.lineEditPassword.textChanged.connect(self.updatePassword)
        self.ui.loginButton.clicked.connect(self.login)



    @Slot()
    def updateID(self) -> int:
        self.ID = self.ui.lineEditID.text()
        return self.ID
    

    @Slot()
    def updatePassword(self) -> int: 
        self.password = self.ui.lineEditPassword.text()
        return self.password

    @Slot()
    def login(self) -> int:
        base_api = "http://localhost:8000"
        try:
            id = str(self.ID)
            pw = str(self.password)
        except AttributeError as e:
            return None
        
        
        resp: requests.Response = requests.get(base_api + "/validate/" + id + "/" + pw)

        if(resp == None):
            return None
        
        if(resp == False):
            return None

        return id





if __name__ == "__main__":
    update_thread = threading.Thread(target=update, daemon=True)
    update_thread.start()
    app = QApplication(sys.argv)
    widget = LoginWindow()
    widget.show()
    sys.exit(app.exec())
