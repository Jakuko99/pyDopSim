from PyQt5.QtWidgets import QWidget, QLabel, QScrollArea, QMainWindow, QMenu, QAction
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from uuid import UUID
import logging
import os

from game.data_types.api_package import Tracks
from game.objects.api_package import TrainObject, Consist
from game.data_types.api_package import TrainType
from game.dialogs.new_train_dialog import NewTrainDialog


class PlatformWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.create_train_dialog = NewTrainDialog(
            self, on_confirm=self.add_created_train
        )
        self.logger = logging.getLogger("App.StationPlatforms")
        plaform_pixmap = QPixmap("assets/station_platforms.png")
        self.setFixedSize(plaform_pixmap.width(), 450)
        self.label = QLabel(self)
        self.label.setPixmap(plaform_pixmap)
        self.label.move(0, 0)
        self.label.setFixedSize(plaform_pixmap.width(), 450)
        self.trains: dict[UUID, Consist] = dict()

        self.context_menu = QMenu(self)
        self.add_consist_action = QAction("Pridať vlak", self)
        # self.add_consist_action.setIcon(QIcon("assets/shunting_icon.png"))
        self.add_consist_action.triggered.connect(self.create_train_dialog.show)
        self.context_menu.addAction(self.add_consist_action)

        self.free_track_action = QAction("Uvoľniť koľaj", self)
        # self.free_track_action.setIcon(QIcon("assets/shunting_icon.png"))
        self.context_menu.addAction(self.free_track_action)

        self.add_consist_4 = QLabel(self)
        self.add_consist_4.setFixedSize(2940, 45)
        self.add_consist_4.move(3438, 340)
        self.add_consist_4.contextMenuEvent = self.context_menu_event

        self.add_consist_4a = QLabel(self)
        self.add_consist_4a.setFixedSize(1050, 45)
        self.add_consist_4a.move(6810, 340)
        self.add_consist_4a.contextMenuEvent = self.context_menu_event

    def add_created_train(self, consist: Consist, track_nr: Tracks, track_pos: int = 0):
        consist.setParent(self)
        self.trains[consist.uuid] = (
            consist  # TODO: need to create custom layout for adding trains dynamically
        )
        self.add_train(track_nr, track_pos, consist)

    def add_train(
        self,
        track_nr: Tracks,
        track_pos: int,
        train: Consist,
    ):
        train.setParent(self)
        self.trains[train.uuid] = train
        if track_nr == Tracks.MANIPULACNA_4A:
            self.trains[train.uuid].move(6800 + track_pos, track_nr.value)
        elif track_nr == Tracks.DOPRAVNA_1:
            self.trains[train.uuid].move(3055 + track_pos, track_nr.value)
        else:
            self.trains[train.uuid].move(3438 + track_pos, track_nr.value)

        self.logger.debug(
            f"Train {train.uuid} added to {track_nr.name} at position {track_pos}"
        )
        train.update()
        self.update()  # not working

    def context_menu_event(self, event):
        self.context_menu.exec_(event.globalPos())


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

        # ----- test consists -----
        con = Consist()
        con1 = Consist()

        con.add_train_obj(TrainObject("ZSSK_Ameer"))
        con.add_train_obj(TrainObject("ZSSK_Ameer"))
        con.add_train_obj(TrainObject("ZSSK_Ameer"))
        con.add_train_obj(TrainObject("ZSSK_Ameer"))
        con.add_train_obj(TrainObject("757-b2-a"))
        con.set_train_number(TrainType.R, 940)

        con1.add_train_obj(TrainObject("757-b2-a"))
        con1.add_train_obj(TrainObject("ZSSK_Ameer"))
        con1.add_train_obj(TrainObject("ZSSK_Ameer"))
        con1.add_train_obj(TrainObject("ZSSK_Ameer"))
        con1.add_train_obj(TrainObject("ZSSK_Ameer"))
        con1.set_train_number(TrainType.R, 941)

        co = Consist()
        co.add_train_obj(TrainObject("840_ZSSK_TEZ"))

        self.platforms.add_train(Tracks.DOPRAVNA_2, 0, con)
        self.platforms.add_train(Tracks.DOPRAVNA_1, 0, con1)
        self.platforms.add_train(
            Tracks.MANIPULACNA_4A,
            0,
            co,
        )

    def get_tracks(self) -> PlatformWidget:
        return self.platforms
