from PyQt5.QtWidgets import QWidget, QLabel, QMessageBox
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtCore import Qt
import logging

from .qt_components import api_package as components


class ControlledStation(QWidget):
    def __init__(self, station_name: str, parent=None, standalone: bool = False):
        super().__init__(parent)
        self.setFixedSize(640, 208)
        self.station_name: str = station_name
        self.doz_active: bool = False

        self.track_layout = QLabel(self)
        self.track_layout.setPixmap(QPixmap("assets/jop_dispatcher.bmp"))
        self.track_layout.setScaledContents(True)
        self.track_layout.setGeometry(0, 0, 640, 208)

        if standalone:
            self.logger = logging.getLogger(f"App.DOZ.{station_name}")
            self.logger.setLevel(logging.DEBUG)
            self.setWindowTitle(f"DOZ - {station_name}")
            self.setWindowIcon(QIcon("assets/doz_icon.png"))

            self.alive_indicator = components.AliveIndicator(self)
            self.alive_indicator.move(10, 158)

        self.doz_label = QLabel("DOZ (RE)", self)
        self.doz_label.move(310, 182)
        self.doz_label.setFont(QFont("Arial", 10))
        self.doz_label.setStyleSheet("color: lime")
        self.doz_label.hide()

        # ----- Custom components -----
        self.jop_button = components.DispatcherStationButton(self)
        self.jop_button.move(264, 180)

        self.jop_button.take_over_action.triggered.connect(self.activate_doz)

        self.station_label = QLabel(self.station_name, self)
        self.station_label.move(0, 0)
        self.station_label.setFixedSize(640, 25)
        self.station_label.setStyleSheet("color: white")
        self.station_label.setFont(QFont("Consolas", 11))
        self.station_label.setAlignment(Qt.AlignCenter)

    def show(self):
        if hasattr(self, "logger"):
            self.logger.info("Starting DOZ GUI")

        super().show()

    def activate_doz(self):
        if self.doz_active:
            self.doz_active = False
            self.doz_label.hide()
            self.jop_button.go_offline()
        else:
            self.doz_active = True
            self.doz_label.show()
            self.jop_button.go_online()
