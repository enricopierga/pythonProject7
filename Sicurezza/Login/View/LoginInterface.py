

from PyQt5 import QtCore, QtGui, QtWidgets


class LoginInterface(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1027, 679)
        MainWindow.setStyleSheet("")
        MainWindow.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 70, 461, 521))
        self.label.setStyleSheet("background-color: rgb(255, 255, 152);\n"
"border-radius: 20px;\n"
"border: 2px solid black;\n"
"\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(410, 10, 181, 151))
        self.label_2.setStyleSheet("image: url(:/newPrefix/logo.png.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(360, 160, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.logbutton = QtWidgets.QPushButton(self.centralwidget)
        self.logbutton.setGeometry(QtCore.QRect(430, 490, 161, 71))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.logbutton.setFont(font)
        self.logbutton.setStyleSheet("QPushButton{\n"
"border-radius: 10px;\n"
"background-color: rgb(221, 214, 73);\n"
"border: 2px solid black;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 255, 155);\n"
"}\n"
"")
        self.logbutton.setObjectName("logbutton")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(300, 240, 51, 51))
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 152);\n"
"\n"
"image: url(:/newPrefix/username-removebg-preview.png);")
        self.label_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_8.setMidLineWidth(0)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(300, 320, 51, 61))
        self.label_9.setStyleSheet("background-color: rgb(255, 255, 152);\n"
"image: url(:/newPrefix/passowrd.png);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 1031, 681))
        self.label_3.setStyleSheet("background-image: url(:/newPrefix/camposfondo.png.jpeg);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(360, 210, 281, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.username = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.username.setFont(font)
        self.username.setStyleSheet("background-color: rgb(221, 214, 73);\n"
"border-radius: 10px;\n"
"border: 2px solid black;")
        self.username.setObjectName("username")
        self.verticalLayout.addWidget(self.username)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.password = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.password.setFont(font)
        self.password.setStyleSheet("background-color: rgb(221, 214, 73);\n"
"border-radius: 10px;\n"
"border: 2px solid black;")
        self.password.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.verticalLayout.addWidget(self.password)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.mostrapasscheck = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.mostrapasscheck.setFont(font)
        self.mostrapasscheck.setObjectName("mostrapasscheck")
        self.verticalLayout.addWidget(self.mostrapasscheck)
        self.label_3.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_5.raise_()
        self.logbutton.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.verticalLayoutWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "Centro Sportivo \"UNIVPM\""))
        self.logbutton.setText(_translate("MainWindow", "LOGIN"))
        self.label_6.setText(_translate("MainWindow", "Username"))
        self.label_7.setText(_translate("MainWindow", "Password"))
        self.mostrapasscheck.setText(_translate("MainWindow", "Mostra Password"))

