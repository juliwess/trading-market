# This Python file uses the following encoding: utf-8
import sys
import requests
import time
import pandas
import threading
from PySide6 import QtCore
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Slot, Qt, QPointF
from PySide6.QtGui import QPainter
from PySide6.QtCharts import QChart, QChartView, QLineSeries
from loginwindow import LoginWindow
from ui_mainwindow import Ui_MainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic mainwindow.ui -o ui_mainwindow.py, or
#     pyside2-uic form.ui -o ui_form.py
def update():
    while(True):
        requests.get("http://localhost:8000/refresh-values")
        time.sleep(5)




class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        #setup the UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #create a loginWindfow
        self.login = LoginWindow()

        self.series = QLineSeries()
        self.series2 = QLineSeries()
        self.series3 = QLineSeries()
        self.series4 = QLineSeries()
        self.series5 = QLineSeries()
        self.series6 = QLineSeries()

    
        #create a chart for the chartpage
        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.addSeries(self.series2)
        self.chart.addSeries(self.series3)
        self.chart.addSeries(self.series4)
        self.chart.addSeries(self.series5)

        self.chart.legend().hide()
        self.chart.setTitle("Values")
        self.chart.createDefaultAxes()
        self.chartView = QChartView(self.chart)
        self.chartView.setRenderHint(QPainter.Antialiasing)

        self.ticker = 0

        t = threading.Thread(target=self.append_values, daemon=True)
        t.start()
    

        #connect the login and addAccount Button
        self.ui.enterLoginButton.clicked.connect(self.enterLogin)
        self.ui.addAccountButton.clicked.connect(self.enterCreateAccount)

        #The confirm button is to find on the page addAccountPage and confirms
        #the creation of an account
        self.ui.confirmButton.clicked.connect(self.createAccount)

    @Slot()
    def enterLogin(self):
        #switches to the login page
        self.ui.stackedWidget.addWidget(self.login)
        self.ui.stackedWidget.setCurrentWidget(self.login)
    
    @Slot()
    def enterCreateAccount(self):
        #switches to the addAccount page
        self.ui.stackedWidget.addWidget(self.ui.addAccountPage)
        self.ui.stackedWidget.setCurrentWidget(self.ui.addAccountPage)


    @Slot()
    def createAccount(self) -> int:
        new_pw = ""
        new_pw = self.ui.passwordLineEdit.text()
        if new_pw == "":
            return None
        
        base_api = "http://localhost:8000"
        id = requests.get(base_api + "/add-trader").json().get("trader-id")
        self.ui.IDlabel.setText("Your ID is: " + str(id))
        self.ui.IDlabel.setText("Your ID is: " + str(id))
       
        requests.get(base_api + "/set-password/" + str(id) + "/" + new_pw)
        self.ui.stackedWidget.addWidget(self.chartView)
        self.ui.stackedWidget.setCurrentWidget(self.chartView)

        return id
    
    def append_values(self):
        while(True):
            ticker = 0
            goods = requests.get("http://localhost:8000/get-goods").json()
            for key,value in goods.items():
                df = pandas.read_csv('values.csv')
                self.series << QPointF(self.ticker, df.loc[0,"Wood"])
                self.series2 << QPointF(self.ticker, df.loc[0,"Gas"])
                self.series3 << QPointF(self.ticker, df.loc[0,"Chemicals"])
                self.series4 << QPointF(self.ticker, df.loc[0,"Bricks"])
                self.series5 << QPointF(self.ticker, df.loc[0,"Iron"])
                self.series5 << QPointF(self.ticker, df.loc[0,"Oil"])

            
            self.chart.axes(Qt.Horizontal)[-1].setMax(self.ticker)
            self.chart.axes(Qt.Horizontal)[-1].setMin(max(0, self.ticker-20))

            biggest_value = requests.get("http://localhost:8000/get-biggest-value").json().get("value")
            self.chart.axes(Qt.Vertical)[-1].setMax(biggest_value)
            self.chart.axes(Qt.Vertical)[-1].setMin(max(0, self.ticker-20))


            self.ticker += 1
            time.sleep(1)


if __name__ == '__main__':
    update_thread = threading.Thread(target=update, daemon=True)
    update_thread.start()
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()

    sys.exit(app.exec())
