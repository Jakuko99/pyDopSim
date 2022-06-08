from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QGraphicsRectItem, QGraphicsEllipseItem
from PyQt5.QtGui import QBrush, QPen
from PyQt5.QtCore import Qt
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

def addShape(type, x, y, xSize, ySize, pen=QPen(Qt.black), brush=QBrush(Qt.white)):
    if type == "rect":
        rect = QGraphicsRectItem(x, y, xSize, ySize)
        rect.setBrush(brush)
        rect.setPen(pen)
        return rect
    elif type == "ellipse":
        ellipse = QGraphicsEllipseItem(x, y, xSize, ySize)
        ellipse.setBrush(brush)
        ellipse.setPen(pen)
        return ellipse
