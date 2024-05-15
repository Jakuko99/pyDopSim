from PyQt5.QtWidgets import QWidget, QLabel, QScrollArea, QMainWindow, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from uuid import UUID
import os

from game.data_types.api_package import Tracks
from game.objects.api_package import Locomotive, Carriage, Consist
from game.data_types.api_package import TrainType


class PlatformWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        plaform_pixmap = QPixmap("assets/station_platforms.png")
        self.setFixedSize(plaform_pixmap.width(), 450)
        self.label = QLabel(self)
        self.label.setPixmap(plaform_pixmap)
        self.label.move(0, 0)
        self.label.setFixedSize(plaform_pixmap.width(), 450)
        self.trains: dict[UUID, Consist] = dict()

    def add_train(
        self,
        track_nr: Tracks,
        track_pos: int,
        train: Consist,
    ):
        self.trains[train.uuid] = train
        if track_nr == Tracks.MANIPULACNA_4A:
            self.trains[train.uuid].move(6800 + track_pos, track_nr.value)
        elif track_nr == Tracks.DOPRAVNA_1:
            self.trains[train.uuid].move(3055 + track_pos, track_nr.value)
        else:
            self.trains[train.uuid].move(3435 + track_pos, track_nr.value)


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
        self.setFixedHeight(475)
        self.setGeometry(120, 150, 1000, 475)
        self.setWindowTitle(f"Staničné koľaje: žst. {station_name}")

        con = Consist(parent=self.platforms)
        con1 = Consist(parent=self.platforms, train_nr=602)

        con.add_carriage(Carriage("ZSSK_Ameer"))
        con.add_carriage(Carriage("ZSSK_Ameer"))
        con.add_carriage(Carriage("ZSSK_Ameer"))
        con.add_carriage(Carriage("ZSSK_Ameer"))
        con.add_locomotive(Locomotive("757-b2-a"))
        con.set_train_number(TrainType.R, 940)

        con1.add_locomotive(Locomotive("757-b2-a"))
        con1.add_carriage(Carriage("ZSSK_Ameer"))
        con1.add_carriage(Carriage("ZSSK_Ameer"))
        con1.add_carriage(Carriage("ZSSK_Ameer"))
        con1.add_carriage(Carriage("ZSSK_Ameer"))

        co = Consist(parent=self.platforms)
        co.add_locomotive(Locomotive("840_ZSSK_TEZ"))

        self.platforms.add_train(Tracks.DOPRAVNA_2, 0, con)
        self.platforms.add_train(Tracks.DOPRAVNA_1, 0, con1)
        self.platforms.add_train(
            Tracks.MANIPULACNA_4A,
            0,
            co,
        )

    def get_tracks(self) -> PlatformWidget:
        return self.platforms
