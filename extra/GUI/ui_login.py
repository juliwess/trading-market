# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(235, 223)
        self.layoutWidget = QWidget(LoginWindow)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 60, 201, 101))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEditID = QLineEdit(self.layoutWidget)
        self.lineEditID.setObjectName(u"lineEditID")

        self.horizontalLayout.addWidget(self.lineEditID)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEditPassword = QLineEdit(self.layoutWidget)
        self.lineEditPassword.setObjectName(u"lineEditPassword")

        self.horizontalLayout_2.addWidget(self.lineEditPassword)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.loginButton = QPushButton(self.layoutWidget)
        self.loginButton.setObjectName(u"loginButton")

        self.verticalLayout_2.addWidget(self.loginButton)


        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"LoginWindow", None))
        self.label.setText(QCoreApplication.translate("LoginWindow", u"ID:", None))
        self.lineEditID.setText("")
        self.label_2.setText(QCoreApplication.translate("LoginWindow", u"Password:", None))
        self.loginButton.setText(QCoreApplication.translate("LoginWindow", u"Login", None))
    # retranslateUi

