from PyQt5.QtWidgets import QWidget, QLabel, QPushButton
from PyQt5.QtCore import Qt, QTimer


class AbstractButton(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.setGeometry(0, 0, 60, 60)

        self.button = QPushButton(self)
        self.button.setFixedSize(40, 40)
        self.button.setStyleSheet(
            "background-color: rgb(175, 169, 153); border-radius: 20px; border: 5px solid black;"
        )

    def setFunctions(self, left_click_function, right_click_function):
        self.button.clicked.connect(left_click_function)
        self.right_click_function = right_click_function

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.RightButton:
            self.right_click_function()
