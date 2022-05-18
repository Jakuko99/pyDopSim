from PyQt5.QtWidgets import QDialog, QPushButton, QLineEdit, QLabel
from PyQt5.QtCore import Qt
from PyQt5 import QtGui

class entryWindow(QDialog):
    def __init__(self):
        pass

    def showWindow(self, name):
        self.exitFlag = False
        self.dialog = QDialog()
        self.dialog.setWindowTitle("Enter value")
        self.dialog.setWindowModality(Qt.ApplicationModal)
        self.field = QLineEdit(self.dialog)
        self.field.move(0,20)
        label = QLabel(self.dialog)
        label.setText(name)
        label.resize(225,20)
        label.setFont(QtGui.QFont("MS Shell Dlg 2", 10))
        label.move(0,0)
        submit = QPushButton("Submit", self.dialog)
        submit.move(0,45)
        submit.clicked.connect(lambda: self.getText())
        cancel = QPushButton("Cancel", self.dialog)
        cancel.move(100,45)
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
            self.text = self.field.text()
            self.dialog.close()
        return self.text