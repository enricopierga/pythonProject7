# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomeGestioneDipendenti.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from GestioneDatabase.QueryGestioneDipendenti.TableDipendenti import TableDipendenti


class HomeGestioneDipUI(object):
    def setupUi(self, MainWindow):
        self.tableDip = TableDipendenti()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1907, 1202)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tornahome = QtWidgets.QCommandLinkButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.tornahome.setFont(font)
        self.tornahome.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tornahome.setObjectName("tornahome")
        self.gridLayout.addWidget(self.tornahome, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.aggiungidip = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.aggiungidip.setFont(font)
        self.aggiungidip.setStyleSheet("QPushButton{\n"
"border-radius: 20px;\n"
"background-color: rgb(221, 214, 73);\n"
"border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 255, 155);\n"
"}\n"
"")
        self.aggiungidip.setObjectName("aggiungidip")
        self.gridLayout.addWidget(self.aggiungidip, 2, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.tabelladip = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabelladip.sizePolicy().hasHeightForWidth())
        self.tabelladip.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tabelladip.setFont(font)
        self.tabelladip.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(221, 214, 73);\n"
"border: 2px solid white;")
        self.tabelladip.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tabelladip.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tabelladip.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tabelladip.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tabelladip.setObjectName("tabelladip")
        self.tabelladip.setColumnCount(9)
        self.tabelladip.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        item.setFont(font)
        self.tabelladip.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        item.setFont(font)
        self.tabelladip.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabelladip.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabelladip.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabelladip.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabelladip.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabelladip.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabelladip.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabelladip.setHorizontalHeaderItem(8, item)
        self.gridLayout.addWidget(self.tabelladip, 1, 0, 1, 2)
        self.modificainfodip = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        self.modificainfodip.setFont(font)
        self.modificainfodip.setStyleSheet("QPushButton{\n"
"border-radius: 20px;\n"
"background-color: rgb(221, 214, 73);\n"
"border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 255, 155);\n"
"}\n"
"")
        self.modificainfodip.setObjectName("modificainfodip")
        self.gridLayout.addWidget(self.modificainfodip, 2, 1, 1, 1)
        self.eliminadip = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        self.eliminadip.setFont(font)
        self.eliminadip.setStyleSheet("QPushButton{\n"
"border-radius: 20px;\n"
"background-color: rgb(221, 214, 73);\n"
"border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 255, 155);\n"
"}\n"
"")
        self.eliminadip.setObjectName("eliminadip")
        self.gridLayout.addWidget(self.eliminadip, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.loadData()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tornahome.setText(_translate("MainWindow", "Torna alla Home"))
        self.label_2.setText(_translate("MainWindow", "Lista Dipendenti:"))
        self.aggiungidip.setText(_translate("MainWindow", " Aggiungi Dipendente"))
        item = self.tabelladip.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "CF"))
        item = self.tabelladip.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nome"))
        item = self.tabelladip.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Cognome"))
        item = self.tabelladip.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Citt??"))
        item = self.tabelladip.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Telefono"))
        item = self.tabelladip.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Mansione"))
        item = self.tabelladip.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Ore Sett."))
        item = self.tabelladip.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Stipendio"))
        item = self.tabelladip.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Username"))
        self.modificainfodip.setText(_translate("MainWindow", "Modifica Info Dipendente"))
        self.eliminadip.setText(_translate("MainWindow", " Elimina Dipendente"))
        self.tabelladip.setColumnWidth(0, 200)
        self.tabelladip.setColumnWidth(1, 200)
        self.tabelladip.setColumnWidth(2, 230)
        self.tabelladip.setColumnWidth(3, 200)
        self.tabelladip.setColumnWidth(4, 200)
        self.tabelladip.setColumnWidth(5, 200)
        self.tabelladip.setColumnWidth(6, 150)
        self.tabelladip.setColumnWidth(7, 240)
        self.tabelladip.setColumnWidth(8, 200)




    def loadData(self):
        subquery = "SELECT * FROM Dipendenti"
        rowindex = 0

        self.tabelladip.setRowCount(30)

        for row in self.tableDip.c.execute(subquery):
            self.tabelladip.setItem(rowindex, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tabelladip.setItem(rowindex, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tabelladip.setItem(rowindex, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.tabelladip.setItem(rowindex, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.tabelladip.setItem(rowindex, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.tabelladip.setItem(rowindex, 5, QtWidgets.QTableWidgetItem(row[5]))
            ore_sett = row[6]
            converted_ore = str(ore_sett)
            self.tabelladip.setItem(rowindex, 6, QtWidgets.QTableWidgetItem(converted_ore))
            stip = row[7]
            converted_stip = str(stip)
            euro = "???"
            self.tabelladip.setItem(rowindex, 7, QtWidgets.QTableWidgetItem(converted_stip + " " +euro))
            self.tabelladip.setItem(rowindex, 8, QtWidgets.QTableWidgetItem(row[8]))

            rowindex += 1

        self.tableDip.conn.commit()



