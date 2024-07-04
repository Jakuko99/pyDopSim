from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon


class AbstractTelephoneButton(QWidget):
    def __init__(self, parent=None):
        self._parent = parent
        QWidget.__init__(self, parent=parent)

        self.setGeometry(0, 0, 55, 55)
        self.setToolTip("Staničný telefón")
        self.setToolTipDuration(750)

        self.button = QPushButton(self)
        icon = QIcon("assets/phone_icon.png")
        self.button.setIconSize(QSize(55, 55))
        self.button.setIcon(icon)
        self.button.move(0, 0)
        self.button.setFixedSize(55, 55)

    def set_click_function(
        self,
        left_click_function,
    ):
        self.button.clicked.connect(left_click_function)
