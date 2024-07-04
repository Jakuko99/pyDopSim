from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon

from game.data_types.api_package import ButtonType


class AbstractButton(QWidget):
    def __init__(self, button_type: ButtonType = ButtonType.NORMAL, parent=None):
        QWidget.__init__(self, parent=parent)
        self.setGeometry(0, 0, 40, 40)
        self.setToolTip(
            "ĽTM - stlačiť, PTM - povytiahnuť, STM - obsluha núdzovej funkcie"
        )
        self.setToolTipDuration(750)
        self.right_click_function = lambda: None
        self.middle_click_function = lambda: None

        self.button = QPushButton(self)
        icon = QIcon("assets/normal_button.png")
        self.button.setIcon(icon)
        self.button.move(0, 0)
        self.button.setFixedSize(40, 40)
        self.button.setStyleSheet("border-radius: 20px;")
        self.button.setIconSize(QSize(40, 40))

    def setFunctions(
        self,
        left_click_function,
        right_click_function,
        middle_click_function=lambda: None,
    ):
        self.button.clicked.connect(left_click_function)
        self.right_click_function = right_click_function
        self.middle_click_function = middle_click_function

    def set_onPress(self, function):
        self.button.pressed.connect(function)

    def set_onRelease(self, function):
        self.button.released.connect(function)

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.RightButton:
            self.right_click_function()
        if QMouseEvent.button() == Qt.MiddleButton:
            self.middle_click_function()
