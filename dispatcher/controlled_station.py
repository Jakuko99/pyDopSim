from PyQt5.QtWidgets import QWidget, QLabel, QMessageBox
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt

from .qt_components import api_package as components


class ControlledStation(QWidget):
    def __init__(self, station_name: str, parent=None):
        super().__init__(parent)
        self.setFixedSize(640, 208)
        self.setFont(QFont("Consolas", 10))
        self.station_name: str = station_name

        self.track_layout = QLabel(self)
        self.track_layout.setPixmap(QPixmap("assets/jop_dispatcher.bmp"))
        self.track_layout.setGeometry(0, 0, 640, 208)

        self.station_label = QLabel(self.station_name, self)
        self.station_label.move(0, 0)
        self.station_label.setFixedSize(640, 25)
        self.station_label.setStyleSheet("color: white")
        self.station_label.setAlignment(Qt.AlignCenter)
