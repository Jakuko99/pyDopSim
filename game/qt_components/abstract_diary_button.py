from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon


class AbstractDiaryButton(QWidget):
    def __init__(self, parent=None):
        self._parent = parent
        QWidget.__init__(self, parent=parent)

        self.setGeometry(0, 0, 65, 80)
        self.setToolTip("Dopravný denník")
        self.setToolTipDuration(750)

        self.button = QPushButton(self)
        icon = QIcon("assets/traffic_diary_icon.png")
        self.button.setIconSize(QSize(65, 80))
        self.button.setIcon(icon)
        self.button.move(0, 0)
        self.button.setFixedSize(65, 80)

    def set_click_function(
        self,
        left_click_function,
    ):
        self.button.clicked.connect(left_click_function)
