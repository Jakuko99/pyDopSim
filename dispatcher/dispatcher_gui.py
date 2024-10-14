from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QFont, QIcon, QPixmap
import logging

from .controlled_station import ControlledStation


class DispatcherGUI(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Dispečerská aplikácia")
        self.setWindowIcon(QIcon("assets/app_icon.png"))
        self.setFont(QFont("Consolas", 11))
        self.setStyleSheet("background-color: black; color: white")
        self.logger = logging.getLogger("App.Dispatcher")

        self.station1 = ControlledStation(parent=self, station_name="Stanica 1")
        self.station1.move(0, 0)

        self.station2 = ControlledStation(parent=self, station_name="Stanica 2")
        self.station2.move(640, 0)

        self.station3 = ControlledStation(parent=self, station_name="Stanica 3")
        self.station3.move(1280, 0)

        self.station4 = ControlledStation(parent=self, station_name="Stanica 4")
        self.station4.move(0, 208)

        self.station5 = ControlledStation(parent=self, station_name="Stanica 5")
        self.station5.move(640, 208)

        self.station6 = ControlledStation(parent=self, station_name="Stanica 6")
        self.station6.move(1280, 208)

        self.station7 = ControlledStation(parent=self, station_name="Stanica 7")
        self.station7.move(0, 416)

        self.station8 = ControlledStation(parent=self, station_name="Stanica 8")
        self.station8.move(640, 416)

        self.station9 = ControlledStation(parent=self, station_name="Stanica 9")
        self.station9.move(1280, 416)

        self.station10 = ControlledStation(parent=self, station_name="Stanica 10")
        self.station10.move(0, 624)

        self.station11 = ControlledStation(parent=self, station_name="Stanica 11")
        self.station11.move(640, 624)

        self.station12 = ControlledStation(parent=self, station_name="Stanica 12")
        self.station12.move(1280, 624)

        self.station13 = ControlledStation(parent=self, station_name="Stanica 13")
        self.station13.move(0, 832)

        self.station14 = ControlledStation(parent=self, station_name="Stanica 14")
        self.station14.move(640, 832)

        self.station15 = ControlledStation(parent=self, station_name="Stanica 15")
        self.station15.move(1280, 832)

        self.full_screen_button = QPushButton("Ukončiť", self)
        self.full_screen_button.move(0, 0)
        self.full_screen_button.clicked.connect(self.close)

    def show(self):
        self.logger.info("DispatcherGUI started")
        # self.showFullScreen()
        self.logger.debug(f"Current screen size: {self.size()}")
