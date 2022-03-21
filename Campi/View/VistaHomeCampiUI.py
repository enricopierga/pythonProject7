# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VistaCampiProvvisoria.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date

class VistaHomeCampiUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1408, 781)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, -1, 33, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.setora = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.setora.setFont(font)
        self.setora.setStyleSheet("\n"
"border-radius: 1px;\n"
"background-color: rgb(221, 214, 73);\n"
"border: 3px solid white;\n"
"\n"
"\n"
"")
        self.setora.setObjectName("setora")
        self.setora.addItem("")
        self.setora.addItem("")
        self.setora.addItem("")
        self.setora.addItem("")
        self.setora.addItem("")
        self.setora.addItem("")
        self.setora.addItem("")
        self.setora.addItem("")
        self.setora.addItem("")
        self.setora.addItem("")
        self.setora.addItem("")
        self.setora.addItem("")
        self.gridLayout.addWidget(self.setora, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.setcampo = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.setcampo.setFont(font)
        self.setcampo.setStyleSheet("\n"
"border-radius: 1px;\n"
"background-color: rgb(221, 214, 73);\n"
"border: 3px solid white;\n"
"\n"
"\n"
"")
        self.setcampo.setObjectName("setcampo")
        self.setcampo.addItem("")
        self.setcampo.addItem("")
        self.setcampo.addItem("")
        self.setcampo.addItem("")
        self.setcampo.addItem("")
        self.gridLayout.addWidget(self.setcampo, 2, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 3, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(54, -1, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.prenotacampo = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prenotacampo.sizePolicy().hasHeightForWidth())
        self.prenotacampo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.prenotacampo.setFont(font)
        self.prenotacampo.setStyleSheet("QPushButton{\n"
"border-radius: 10px;\n"
"background-color: rgb(221, 214, 73);\n"
"border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 255, 155);\n"
"}")
        self.prenotacampo.setObjectName("prenotacampo")
        self.gridLayout_2.addWidget(self.prenotacampo, 1, 0, 1, 1, QtCore.Qt.AlignBottom)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        self.eliminaprenotazione = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eliminaprenotazione.sizePolicy().hasHeightForWidth())
        self.eliminaprenotazione.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.eliminaprenotazione.setFont(font)
        self.eliminaprenotazione.setStyleSheet("QPushButton{\n"
"border-radius: 10px;\n"
"background-color: rgb(221, 214, 73);\n"
"border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 255, 155);\n"
"}")
        self.eliminaprenotazione.setObjectName("eliminaprenotazione")
        self.gridLayout_2.addWidget(self.eliminaprenotazione, 1, 1, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.gridLayout_3.addLayout(self.gridLayout_2, 3, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 75, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.campitennis = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.campitennis.setFont(font)
        self.campitennis.setStyleSheet("background-color: rgb(255, 104, 16);\n"
"border-radius: 10px;")
        self.campitennis.setObjectName("campitennis")
        self.campitennis.setColumnCount(2)
        self.campitennis.setRowCount(13)
        item = QtWidgets.QTableWidgetItem()
        self.campitennis.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.campitennis.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.campitennis.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.campitennis.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.campitennis.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.campitennis.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.campitennis.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.campitennis.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.campitennis.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.campitennis.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.campitennis.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.campitennis.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.campitennis.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 98, 20))
        self.campitennis.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.campitennis.setHorizontalHeaderItem(1, item)
        self.horizontalLayout.addWidget(self.campitennis)
        self.campipadel = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.campipadel.setFont(font)
        self.campipadel.setAcceptDrops(False)
        self.campipadel.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(49, 121, 255);")
        self.campipadel.setObjectName("campipadel")
        self.campipadel.setColumnCount(2)
        self.campipadel.setRowCount(13)
        item = QtWidgets.QTableWidgetItem()
        self.campipadel.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.campipadel.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.campipadel.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.campipadel.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.campipadel.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.campipadel.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.campipadel.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.campipadel.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.campipadel.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.campipadel.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.campipadel.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.campipadel.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.campipadel.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 98, 20))
        self.campipadel.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.campipadel.setHorizontalHeaderItem(1, item)
        self.horizontalLayout.addWidget(self.campipadel)
        self.calcetto = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calcetto.sizePolicy().hasHeightForWidth())
        self.calcetto.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.calcetto.setFont(font)
        self.calcetto.setStyleSheet("border-radius: 10px;\n"
"\n"
"background-color: rgb(141, 255, 47);")
        self.calcetto.setObjectName("calcetto")
        self.calcetto.setColumnCount(1)
        self.calcetto.setRowCount(13)
        item = QtWidgets.QTableWidgetItem()
        self.calcetto.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.calcetto.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.calcetto.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.calcetto.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.calcetto.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.calcetto.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.calcetto.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.calcetto.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.calcetto.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.calcetto.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.calcetto.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.calcetto.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.calcetto.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 98, 20))
        self.calcetto.setHorizontalHeaderItem(0, item)
        self.horizontalLayout.addWidget(self.calcetto)
        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 0, 1, 3)
        self.tornahome = QtWidgets.QCommandLinkButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tornahome.sizePolicy().hasHeightForWidth())
        self.tornahome.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.tornahome.setFont(font)
        self.tornahome.setStyleSheet("background-color: rgb(255, 255, 255);")
        icon = QtGui.QIcon.fromTheme("null")
        self.tornahome.setIcon(icon)
        self.tornahome.setObjectName("tornahome")
        self.gridLayout_3.addWidget(self.tornahome, 3, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.annomesegiorno = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.annomesegiorno.sizePolicy().hasHeightForWidth())
        self.annomesegiorno.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.annomesegiorno.setFont(font)
        self.annomesegiorno.setObjectName("annomesegiorno")
        self.gridLayout_3.addWidget(self.annomesegiorno, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.setora.setItemText(0, _translate("MainWindow", "9-10"))
        self.setora.setItemText(1, _translate("MainWindow", "10-11"))
        self.setora.setItemText(2, _translate("MainWindow", "11-12"))
        self.setora.setItemText(3, _translate("MainWindow", "12-13"))
        self.setora.setItemText(4, _translate("MainWindow", "13-14"))
        self.setora.setItemText(5, _translate("MainWindow", "14-15"))
        self.setora.setItemText(6, _translate("MainWindow", "15-16"))
        self.setora.setItemText(7, _translate("MainWindow", "16-17"))
        self.setora.setItemText(8, _translate("MainWindow", "17-18"))
        self.setora.setItemText(9, _translate("MainWindow", "18-19"))
        self.setora.setItemText(10, _translate("MainWindow", "19-20"))
        self.setora.setItemText(11, _translate("MainWindow", "20-21"))
        self.label_7.setText(_translate("MainWindow", "Scegli il campo:"))
        self.setcampo.setItemText(0, _translate("MainWindow", "Campo CENTRALE (Terra Rossa)"))
        self.setcampo.setItemText(1, _translate("MainWindow", "Campo 2 (Terra Rossa)"))
        self.setcampo.setItemText(2, _translate("MainWindow", "Padel 1 "))
        self.setcampo.setItemText(3, _translate("MainWindow", "Padel 2"))
        self.setcampo.setItemText(4, _translate("MainWindow", "Calcetto"))
        self.label_8.setText(_translate("MainWindow", "Scegli la fascia oraria:"))
        self.prenotacampo.setText(_translate("MainWindow", "Prenota"))
        self.label_9.setText(_translate("MainWindow", "Seleziona l\'azione:"))
        self.eliminaprenotazione.setText(_translate("MainWindow", "Elimina Prenotazione"))
        item = self.campitennis.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "9-10"))
        item = self.campitennis.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "10-11"))
        item = self.campitennis.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "11-12"))
        item = self.campitennis.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "12-13"))
        item = self.campitennis.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "13-14"))
        item = self.campitennis.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "14-15"))
        item = self.campitennis.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "15-16"))
        item = self.campitennis.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "16-17"))
        item = self.campitennis.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "17-18"))
        item = self.campitennis.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "18-19"))
        item = self.campitennis.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "19-20"))
        item = self.campitennis.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "20-21"))
        item = self.campitennis.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "21-22"))
        item = self.campitennis.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Campo Centrale"))
        item = self.campitennis.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Campo 2"))
        item = self.campipadel.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "9-10"))
        item = self.campipadel.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "10-11"))
        item = self.campipadel.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "11-12"))
        item = self.campipadel.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "12-13"))
        item = self.campipadel.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "13-14"))
        item = self.campipadel.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "14-15"))
        item = self.campipadel.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "15-16"))
        item = self.campipadel.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "16-17"))
        item = self.campipadel.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "17-18"))
        item = self.campipadel.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "18-19"))
        item = self.campipadel.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "19-20"))
        item = self.campipadel.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "20-21"))
        item = self.campipadel.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "21-22"))
        item = self.campipadel.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Padel 1"))
        item = self.campipadel.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Padel 2"))
        item = self.calcetto.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "9-10"))
        item = self.calcetto.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "10-11"))
        item = self.calcetto.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "11-12"))
        item = self.calcetto.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "12-13"))
        item = self.calcetto.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "13-14"))
        item = self.calcetto.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "14-15"))
        item = self.calcetto.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "15-16"))
        item = self.calcetto.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "16-17"))
        item = self.calcetto.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "17-18"))
        item = self.calcetto.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "18-19"))
        item = self.calcetto.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "19-20"))
        item = self.calcetto.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "20-21"))
        item = self.calcetto.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "21-22"))
        item = self.calcetto.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Calcetto"))
        self.tornahome.setText(_translate("MainWindow", "Torna alla Home"))
        self.annomesegiorno.setText(_translate("MainWindow", "Prova Data"))

        self.campitennis.setColumnWidth(0, 250)
        self.campitennis.setColumnWidth(1, 250)
        self.campipadel.setColumnWidth(0, 250)
        self.campipadel.setColumnWidth(1, 250)
        self.calcetto.setColumnWidth(0,250)



