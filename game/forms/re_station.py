from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QComboBox, QLineEdit
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

from game.qt_components.api_package import (
    AbstractSignal,
    AbstractTrack,
    AbstractSwitch,
    AbstractIndicator,
    AbstractLever,
    AbstractIndicatorSlim,
)
from game.data_types.api_package import (
    SignalSign,
    TrackState,
    SwitchType,
    IndicatorState,
    LeverState,
)


class REStation(QMainWindow):
    def __init__(self, station_name: str):
        super().__init__()
        self.setGeometry(0, 0, 1100, 780)
        self.setWindowTitle("Station test window")
        self.setFixedSize(1100, 780)

        self.font_obj = QFont("Arial", 25)

        self.background = QLabel(self)
        self.background.setPixmap(QPixmap("assets/reliefRE.bmp"))
        self.background.setScaledContents(True)
        self.background.setGeometry(0, 0, 1100, 780)

        self.title = QLabel(station_name, self)
        self.title.move(372, 17)
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setFixedSize(356, 55)
        self.title.setFont(self.font_obj)
