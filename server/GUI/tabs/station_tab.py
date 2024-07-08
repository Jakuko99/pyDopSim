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

from server.objects.api_package import Station
from ..station_view import StationView


class StationTab(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.setFont(QFont("Arial", 11))
        self.stations: dict[str:Station] = dict()

        self.station_name_input = QLineEdit(self)
        self.station_name_input.move(5, 5)
        self.station_name_input.setPlaceholderText("názov stanice")
        self.station_name_input.setFixedWidth(200)

        self.station_name_G_input = QLineEdit(self)
        self.station_name_G_input.move(5, 35)
        self.station_name_G_input.setPlaceholderText("zo stanice")
        self.station_name_G_input.setFixedWidth(200)

        self.station_name_L_input = QLineEdit(self)
        self.station_name_L_input.move(5, 65)
        self.station_name_L_input.setPlaceholderText("v stanici")
        self.station_name_L_input.setFixedWidth(200)

        self.allow_2L_checkbox = QCheckBox("Povoliť 2L", self)
        self.allow_2L_checkbox.move(5, 95)

        self.add_station_button = QPushButton("Pridať stanicu", self)
        self.add_station_button.move(5, 125)

        self.station_list = QListWidget(self)
        self.station_list.move(300, 5)
        self.station_list.setFixedSize(290, 225)
        self.station_list.itemClicked.connect(self.station_list_item_clicked)

        self.remove_station_button = QPushButton("Odstrániť stanicu", self)
        self.remove_station_button.move(445, 235)

        self.show_advanced_checkbox = QCheckBox("Zobraziť rozšírené nastavenia", self)
        self.show_advanced_checkbox.move(5, 155)
        self.show_advanced_checkbox.stateChanged.connect(
            lambda: self.advanced_settings_group.setVisible(
                self.show_advanced_checkbox.isChecked()
            )
        )

        self.station_scheme = StationView(self)
        self.station_scheme.move(50, 250)

        self.advanced_settings_group = QGroupBox(self)
        self.advanced_settings_group.move(5, 180)
        self.advanced_settings_group.setStyleSheet("background-color: white;")
        self.advanced_settings_group.setFixedSize(290, 320)
        self.advanced_settings_group.hide()

        self.load_track_file = QPushButton("Načítať trať", self)
        self.load_track_file.clicked.connect(self.load_track_file_func)
        self.load_track_file.setFixedSize(110, 30)
        self.load_track_file.move(5, 505)

        self.save_track_file = QPushButton("Uložiť trať", self)
        self.save_track_file.clicked.connect(self.save_track_file_func)
        self.save_track_file.setFixedSize(110, 30)
        self.save_track_file.move(120, 505)

    def station_list_item_clicked(self, item):
        station: Station = self.stations.get(item.text(), None)
        if station:
            self.station_scheme.set_station_names(
                name_1L=station.left_station,
                name_2L=station.turn_station,
                name_S=station.right_station,
            )
            self.station_name_input.setText(station.station_name_N)
            self.station_name_G_input.setText(station.station_name_G)
            self.station_name_L_input.setText(station.station_name_L)

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
                        station_type=values["station_type"],
                    )

                for station, inflection in track["inflections"].items():
                    if self.stations.get(station, None):
                        self.stations[station].add_inflections(
                            inflection["genitive"], inflection["local"]
                        )

            self.station_list.clear()
            self.station_list.addItems(self.stations.keys())

            if hasattr(self.parent, "overview_tab"):
                self.parent.overview_tab.update_table(self.stations)

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
