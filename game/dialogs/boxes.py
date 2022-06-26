from PyQt5.QtWidgets import QDialog, QPushButton, QLineEdit, QLabel, QComboBox
from PyQt5.QtCore import Qt
from PyQt5 import QtGui

class entryWindow(QDialog):
    def __init__(self, windowName):
        self.windowName = windowName

    def showWindow(self, *entryTexts):
        self.exitFlag = False
        self.entryCount = len(entryTexts)
        self.entryTexts = entryTexts
        self.dialog = QDialog()
        self.dialog.setWindowTitle(self.windowName)
        self.dialog.setWindowModality(Qt.ApplicationModal)
        self.entries = []
        for x in range(len(entryTexts)):
            self.entries.append(QLineEdit(self.dialog))
            self.entries[x].move(0,20 + x * 45)
            label = QLabel(self.dialog)
            label.setText(entryTexts[x] + ":")
            label.resize(225,20)
            label.setFont(QtGui.QFont("MS Shell Dlg 2", 10))
            label.move(0,0 + x * 45)
        submit = QPushButton("Submit", self.dialog)
        submit.move(0,45 + self.entryCount * 30)
        submit.clicked.connect(lambda: self.getText())
        cancel = QPushButton("Cancel", self.dialog)
        cancel.move(100,45 + self.entryCount * 30)
        cancel.clicked.connect(lambda: self.exit())
        self.dialog.exec_()

    def selectionWindow(self, **kwargs):
        self.exitFlag = False
        self.entryCount = len(kwargs)
        self.dialog = QDialog()
        self.dialog.setWindowTitle(self.windowName)
        self.dialog.setWindowModality(Qt.ApplicationModal)
        self.entries = []
        self.entryTexts = []
        x = 0
        for key, value in kwargs.items():
            self.entryTexts.append(key)
            label = QLabel(self.dialog)
            label.setText(key + ":")
            label.resize(225,20)
            label.setFont(QtGui.QFont("MS Shell Dlg 2", 10))
            label.move(0,x + len(self.entries) * 45)
            self.entries.append(QComboBox(self.dialog))
            self.entries[x].addItems(value)
            self.entries[x].move(0,20 + x * 50)
            x += 1
        submit = QPushButton("Submit", self.dialog)
        submit.move(0,45 + self.entryCount * 30)
        submit.clicked.connect(lambda: self.getText()) # create a function that will return the selected values
        cancel = QPushButton("Cancel", self.dialog)
        cancel.move(100,45 + self.entryCount * 30)
        cancel.clicked.connect(lambda: self.exit())
        self.dialog.exec_()

    def exit(self):
        self.dialog.close()
        self.text = None
        self.exitFlag = True

    def getText(self):
        if self.exitFlag:
            return self.text
        else:
            self.text = [x.text() for x in self.entries]
            self.dialog.close()
        return self.text