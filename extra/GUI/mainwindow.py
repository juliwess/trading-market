# This Python file uses the following encoding: utf-8
import sys
from PySide6 import QtCore
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QWidget
from loginwindow import LoginWindow
from ui_mainwindow import Ui_MainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic mainwindow.ui -o ui_mainwindow.py, or
#     pyside2-uic form.ui -o ui_form.py

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
       


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    wid = LoginWindow()
    wid.show()
    sys.exit(app.exec())
