# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStackedWidget, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(40, 60, 561, 291))
        self.addAccountPage = QWidget()
        self.addAccountPage.setObjectName(u"addAccountPage")
        self.verticalLayout_2 = QVBoxLayout(self.addAccountPage)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.addAccountPage)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.passwordLineEdit = QLineEdit(self.addAccountPage)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")

        self.horizontalLayout_2.addWidget(self.passwordLineEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.confirmButton = QPushButton(self.addAccountPage)
        self.confirmButton.setObjectName(u"confirmButton")

        self.verticalLayout_4.addWidget(self.confirmButton)


        self.verticalLayout_2.addLayout(self.verticalLayout_4)

        self.stackedWidget.addWidget(self.addAccountPage)
        self.mainPage = QWidget()
        self.mainPage.setObjectName(u"mainPage")
        self.verticalLayout = QVBoxLayout(self.mainPage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.mainPage)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.enterLoginButton = QPushButton(self.mainPage)
        self.enterLoginButton.setObjectName(u"enterLoginButton")

        self.horizontalLayout.addWidget(self.enterLoginButton)

        self.addAccountButton = QPushButton(self.mainPage)
        self.addAccountButton.setObjectName(u"addAccountButton")

        self.horizontalLayout.addWidget(self.addAccountButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.stackedWidget.addWidget(self.mainPage)
        self.IDlabel = QLabel(self.centralwidget)
        self.IDlabel.setObjectName(u"IDlabel")
        self.IDlabel.setGeometry(QRect(440, 0, 233, 57))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Set password:", None))
        self.confirmButton.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Trading-Market:", None))
        self.enterLoginButton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.addAccountButton.setText(QCoreApplication.translate("MainWindow", u"Add Account", None))
        self.IDlabel.setText("")
    # retranslateUi

