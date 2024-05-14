from PyQt5.QtWidgets import QWidget, QLabel, QScrollArea, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from uuid import UUID
import os

from game.data_types.api_package import Tracks
from game.objects.api_package import Train, Carriage


class PlatformWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        plaform_pixmap = QPixmap("assets/station_platforms.png")
        self.setFixedSize(plaform_pixmap.width(), 450)
        self.label = QLabel(self)
        self.label.setPixmap(plaform_pixmap)
        self.label.move(0, 0)
        self.label.setFixedSize(plaform_pixmap.width(), 450)
        self.trains: dict[UUID, Train] = dict()

    def add_train(
        self,
        track_nr: Tracks,
        track_pos: int,
        train: Train,
    ):
        self.trains[train.uuid] = train
        if track_nr == Tracks.MANIPULACNA_4A:
            self.trains[train.uuid].move(6805 + track_pos, track_nr.value)
        else:
            self.trains[train.uuid].move(3440 + track_pos, track_nr.value)


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
        # self.setStyleSheet("background-color: #303030;")
        self.setFixedHeight(475)
        self.setGeometry(120, 150, 1000, 475)
        self.setWindowTitle(f"Staničné koľaje: žst. {station_name}")

        train = Train("757-b2-a", 600, self.platforms)
        train.add_carriage(Carriage("ZSSK_Ameer"))
        train.add_carriage(Carriage("ZSSK_Ameer"))
        train.add_carriage(Carriage("ZSSK_Ameer"))
        train.add_carriage(Carriage("ZSSK_Ameer"))

        self.platforms.add_train(
            Tracks.DOPRAVNA_1, 100, Train("0Bee", parent=self.platforms)
        )
        self.platforms.add_train(Tracks.DOPRAVNA_2, 100, train)
        self.platforms.add_train(
            Tracks.DOPRAVNA_3,
            100,
            Train("840_ZSSK_TEZ", parent=self.platforms, train_nr=1822),
        )
        self.platforms.add_train(
            Tracks.DOPRAVNA_5, 100, Train("495-95-a", parent=self.platforms)
        )
        self.platforms.add_train(
            Tracks.MANIPULACNA_4, 100, Train("425-95-c-a", parent=self.platforms)
        )
        self.platforms.add_train(
            Tracks.MANIPULACNA_4A, 300, Train("405-95-L", parent=self.platforms)
        )

    def get_tracks(self) -> PlatformWidget:
        return self.platforms
