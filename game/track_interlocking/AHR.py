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
        self.background.setFixedSize(191, 160)

        self.RBP_button = AbstractButton(parent=self)
        self.RBP_button.move(12 if type == "L" else 137, 85)

        self.UST_button = AbstractButton(parent=self)
        self.UST_button.move(137 if type == "L" else 12, 85)

        self.UVT = AbstractIndicatorSlim(
            parent=self, indicator_color=IndicatorColor.WHITE
        )
        self.UVT.move(77, 28)

        self.UST = AbstractIndicatorSlim(
            parent=self, indicator_color=IndicatorColor.RED
        )
        self.UST.move(15 if type == "S" else 139, 28)

        self.PST = AbstractIndicatorSlim(
            parent=self, indicator_color=IndicatorColor.GREEN
        )
        self.PST.move(139 if type == "S" else 15, 28)
