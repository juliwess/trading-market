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
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_LoginWindow


def update():
    while(True):
        requests.get("http://localhost:8000/refresh-values")
        time.sleep(5)



class LoginWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.ui.loginButton.clicked.connect(login)



@Slot()
def login() -> int:
    base_api = "http://localhost:8000"

    #A trader id must always contain at least one character
    trader_id = ""
    while(trader_id == ""):
        trader_id = input("Enter your ID please")

        #Did the trader enter something that is not a number?
        try:
            int(trader_id)
        except ValueError as e:
            trader_id = ""
            print("Invalid")

    #A password cant't be empty
    pasw = ""
    while(pasw == ""):
            pasw = input("Enter your password")

    #If the result can't be fetched the ID must be invalid
    try:
        requests.get(base_api + "/validate/" + trader_id + "/" + pasw).json().get("result")

    except json.decoder.JSONDecodeError as e:
        print("Invalid trader_id! Please try again")
        login()

    #check wether password and id are compatible
    counter = 0

    # You've got 5 tries to login the loop only runs if you have a low enough amount of tries and enter the wrong password
    while(not requests.get(base_api + "/validate/" + str(trader_id) + "/" + str(pasw)).json().get("result") and counter != 5):
       print("Wrong password")
       print(str(5 - counter) + " try/tries left")
       counter += 1
       pasw = input("Try again: ")
       print(requests.get(base_api + "/validate/" + str(trader_id) + "/" + str(pasw)).json().get("result"))

       #Right pw entered?
       if(requests.get(base_api + "/validate/" + str(trader_id) + "/" + str(pasw)).json().get("result")):
        return trader_id

    # Right pw entered?
    if(requests.get(base_api + "/validate/" + str(trader_id) + "/" + str(pasw)).json().get("result")):
        return trader_id

    #if a trader enters faulty too many times his account will be removed
    print("Too many false tries, your account will be deleted")
    requests.get(base_api + "/remove-trader/" +str(trader_id))
    return trader_id






if __name__ == "__main__":
    update_thread = threading.Thread(target=update, daemon=True)
    update_thread.start()
    app = QApplication(sys.argv)
    widget = LoginWindow()
    widget.show()
    sys.exit(app.exec())
