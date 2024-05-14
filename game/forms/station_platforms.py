from PyQt5.QtWidgets import QWidget, QLabel, QScrollArea, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import os

from game.data_types.api_package import TrackNumbers


class PlatformWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        plaform_pixmap = QPixmap("assets/station_platforms.png")
        self.setFixedSize(plaform_pixmap.width(), 450)
        self.label = QLabel(self)
        self.label.setPixmap(plaform_pixmap)
        self.label.move(0, 0)
        self.label.setFixedSize(plaform_pixmap.width(), 450)
        self.trains: dict = dict()

    def add_train(
        self,
        track_nr: TrackNumbers,
        track_pos: int,
        train_asset: str,
        train_nr: int = None,
    ):
        if os.path.exists(f"assets/vozidla/{train_asset}.bmp"):
            train_pixmap = QPixmap(f"assets/vozidla/{train_asset}.bmp")
            self.trains[track_nr] = QLabel(self)
            self.trains[track_nr].setPixmap(
                train_pixmap
            )  # TODO: needs to implement object for train interaction
            if track_nr == TrackNumbers.MANIPULACNA_4A:
                self.trains[track_nr].move(6805 + track_pos, track_nr.value)
            else:
                self.trains[track_nr].move(3440 + track_pos, track_nr.value)
        else:
            print(f"Train asset {train_asset} not found.")
            return -1  # TODO: implememt logging system later


class StationPlatforms(QMainWindow):
    def __init__(self, station_name: str = "Test station"):
        super().__init__()
        self.station_name = station_name

        self.scroll = QScrollArea()
        self.platforms = PlatformWidget(self)

        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.platforms)

        self.setCentralWidget(self.scroll)
        self.setStyleSheet("background-color: #303030;")
        self.setFixedHeight(500)
        self.setGeometry(120, 150, 1000, 500)
        self.setWindowTitle(f"Staničné koľaje: žst. {station_name}")

        self.platforms.add_train(TrackNumbers.DOPRAVNA_1, 100, "0Bee")
        self.platforms.add_train(TrackNumbers.DOPRAVNA_2, 100, "ZSSK_Ameer")
        self.platforms.add_train(TrackNumbers.DOPRAVNA_3, 100, "840_ZSSK_TEZ")
        self.platforms.add_train(TrackNumbers.DOPRAVNA_5, 100, "495-95-a")
        self.platforms.add_train(TrackNumbers.MANIPULACNA_4, 100, "425-95-c-a")
        self.platforms.add_train(TrackNumbers.MANIPULACNA_4A, 300, "405-95-L")

    def get_tracks(self) -> PlatformWidget:
        return self.platforms
