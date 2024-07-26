from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QPixmap

from game.qt_components.api_package import AbstractButton, AbstractIndicatorSlim
from game.data_types.api_package import IndicatorColor, IndicatorState


class AHR(QWidget):
    def __init__(self, parent=None, type: str = "L"):
        QWidget.__init__(self, parent=parent)
        self.setFixedSize(191, 160)

        self.background = QLabel(self)
        self.background.setPixmap(QPixmap(f"assets/panAHR{type.upper()}black.bmp"))
        self.background.setScaledContents(True)
        self.background.setFixedSize(201, 170)

        self.RBP_button = AbstractButton(parent=self)
        self.RBP_button.move(12 if type == "L" else 145, 90)

        self.UST_button = AbstractButton(parent=self)
        self.UST_button.move(145 if type == "L" else 12, 90)

        self.UVT = AbstractIndicatorSlim(
            parent=self, indicator_color=IndicatorColor.WHITE
        )
        self.UVT.move(80, 33)

        self.UST = AbstractIndicatorSlim(
            parent=self, indicator_color=IndicatorColor.RED
        )
        self.UST.move(15 if type == "S" else 144, 33)

        self.PST = AbstractIndicatorSlim(
            parent=self, indicator_color=IndicatorColor.GREEN
        )
        self.PST.move(144 if type == "S" else 15, 33)
