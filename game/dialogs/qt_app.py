from PyQt5 import QtWidgets, uic
import sys

class PyQt(QtWidgets.QMainWindow):
    def __init__(self, layout):
        super(PyQt, self).__init__()
        uic.loadUi(layout, self)
        self.show()

class PyQtApp:
    def __init__(self, layout : str) -> None:
        self.app = QtWidgets.QApplication(sys.argv)
        self.Dialog = QtWidgets.QMainWindow()
        self.window = PyQt(layout)
    
    def execute(self) -> None:
        self.app.exec_()
    
    def getWindow(self) -> QtWidgets.QMainWindow:
        return self.window

    def getDialog(self) -> QtWidgets.QApplication:
        return self.Dialog
