import os
import json
from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QComboBox,
    QCheckBox,
    QListWidget,
    QLineEdit,
    QGroupBox,
    QFileDialog,
)
from PyQt5.QtGui import QFont, QIntValidator

from ..objects.api_package import Station


class StationTab(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.setFont(QFont("Arial", 11))
        self.stations: dict[str:Station] = dict()

        self.station_name_input = QLineEdit(self)
        self.station_name_input.move(5, 5)
        self.station_name_input.setPlaceholderText("Názov stanice")

        self.station_name_G_input = QLineEdit(self)
        self.station_name_G_input.move(5, 35)
        self.station_name_G_input.setPlaceholderText("zo stanice")

        self.station_name_L_input = QLineEdit(self)
        self.station_name_L_input.move(5, 65)
        self.station_name_L_input.setPlaceholderText("v stanici")

        self.allow_2L_checkbox = QCheckBox("Povoliť 2L", self)
        self.allow_2L_checkbox.move(5, 95)

        self.add_station_button = QPushButton("Pridať stanicu", self)
        self.add_station_button.move(5, 125)

        self.station_list = QListWidget(self)
        self.station_list.move(300, 5)
        self.station_list.setFixedSize(290, 400)

        self.remove_station_button = QPushButton("Odstrániť stanicu", self)
        self.remove_station_button.move(445, 410)

        self.show_advanced_checkbox = QCheckBox("Zobraziť rozšírené nastavenia", self)
        self.show_advanced_checkbox.move(5, 155)
        self.show_advanced_checkbox.stateChanged.connect(
            lambda: self.advanced_settings_group.setVisible(
                self.show_advanced_checkbox.isChecked()
            )
        )

        self.advanced_settings_group = QGroupBox("Rozšírené nastavenia", self)
        self.advanced_settings_group.move(5, 180)
        self.advanced_settings_group.setFixedSize(290, 325)
        self.advanced_settings_group.hide()

        self.load_track_file = QPushButton("Načítať trať", self)
        self.load_track_file.clicked.connect(self.load_track_file_func)
        self.load_track_file.setFixedSize(100, 25)
        self.load_track_file.move(5, 510)

        self.save_track_file = QPushButton("Uložiť trať", self)
        self.save_track_file.clicked.connect(self.save_track_file_func)
        self.save_track_file.setFixedSize(100, 25)
        self.save_track_file.move(110, 510)

    def load_track_file_func(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            caption="Načítať trať",
            filter="JSON súbory (*.json)",
            directory=os.getcwd(),
        )
        if file_name:
            self.parent.logger.debug(f"Loading track file: {file_name}")
            with open(file_name, "r", encoding="utf-8") as f:
                track: dict = json.load(f)
                for station, values in track["stations"].items():
                    self.stations[station] = Station(
                        station_name=station,
                        left_station=values["left_station"],
                        right_station=values["right_station"],
                        turn_station=values["turn_station"],
                    )

            self.station_list.clear()
            self.station_list.addItems(self.stations.keys())

    def save_track_file_func(self):
        file_name, _ = QFileDialog.getSaveFileName(
            self,
            caption="Uložiť trať",
            filter="JSON súbory (*.json)",
            directory=os.getcwd(),
        )
        if file_name:
            self.parent.logger.debug(f"Saving track file: {file_name}")
            pass
