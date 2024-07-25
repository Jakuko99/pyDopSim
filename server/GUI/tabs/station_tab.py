import os
import json
import pandas as pd
from uuid import uuid4
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
    QMessageBox,
)
from PyQt5.QtGui import QFont, QIntValidator

from server.objects.api_package import Station, Route, StationName
from ..station_view import StationView
from utils.api_package import sqlite_handler


class StationTab(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.setFont(QFont("Arial", 11))
        self.stations: pd.DataFrame = pd.DataFrame()

        self.routes_combobox = QComboBox(self)
        self.routes_combobox.move(5, 5)
        self.routes_combobox.setFixedSize(290, 30)

        self.station_list = QListWidget(self)
        self.station_list.move(5, 40)
        self.station_list.setFixedSize(290, 240)
        self.station_list.itemClicked.connect(self.station_list_item_clicked)

        self.station_scheme = StationView(self)
        self.station_scheme.move(50, 260)

        self.load_track_file = QPushButton("Načítať trať", self)
        self.load_track_file.clicked.connect(self.load_track_file_func)
        self.load_track_file.setFixedSize(110, 30)
        self.load_track_file.move(5, 505)

        self.save_track_file = QPushButton("Vymazať trať", self)
        self.save_track_file.clicked.connect(self.remove_track_func)
        self.save_track_file.setFixedSize(110, 30)
        self.save_track_file.move(120, 505)

        self.fetch_data_from_db()
        self.routes_combobox.currentIndexChanged.connect(
            self.route_combobox_changed
        )  # prevent duplicate calls

    def fetch_data_from_db(self):
        self.routes_combobox.clear()
        self.station_list.clear()

        with sqlite_handler.get_connection() as cur:
            routes = pd.read_sql("SELECT * FROM routes", cur)
            self.stations = pd.read_sql("SELECT * FROM stations", cur)

            self.parent.logger.debug(
                f"Loaded {len(self.stations)} stations from database"
            )

            if not routes.empty:
                station_per_route = self.stations.groupby("route_uid").size()
                for route in routes.itertuples():
                    self.routes_combobox.addItem(
                        f"{route.route_name} ({station_per_route.get(route.uid, 0)})"
                    )
                self.station_list.addItems(
                    self.stations.loc[
                        self.stations["route_uid"] == routes.iloc[0]["uid"],
                        "station_name",
                    ].to_list()
                )

    def station_list_item_clicked(self, item):
        self.station_scheme.set_station_names(
            name_1L=self.stations.loc[
                self.stations["station_name"] == item.text(), "left_station"
            ].values[0],
            name_2L=self.stations.loc[
                self.stations["station_name"] == item.text(), "turn_station"
            ].values[0],
            name_S=self.stations.loc[
                self.stations["station_name"] == item.text(), "right_station"
            ].values[0],
        )

    def route_combobox_changed(self, index):
        if index == -1:
            return

        self.station_list.clear()

        with sqlite_handler.get_cursor() as cur:
            route_name = self.routes_combobox.currentText().split(" ")[0]
            route_uid = cur.execute(
                f"SELECT uid FROM routes WHERE route_name = '{route_name}'"
            ).fetchone()[0]

        self.station_list.addItems(
            self.stations.loc[
                self.stations["route_uid"] == route_uid, "station_name"
            ].to_list()
        )

    def load_track_file_func(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            caption="Načítať trať",
            filter="JSON súbory (*.json)",
            directory=os.getcwd(),
        )
        if file_name:
            self.parent.logger.debug(f"Loading route file: {file_name}")
            with open(file_name, "r", encoding="utf-8") as f:
                try:
                    track: dict = json.load(f)
                    new_route = Route()
                    new_route.uid = uuid4()
                    new_route.route_name = track["route"]["name"]

                    with sqlite_handler.get_cursor() as cur:
                        if (
                            cur.execute(
                                f"SELECT COUNT(*) FROM routes WHERE route_name = '{new_route.route_name}';"
                            ).fetchone()[0]
                            == 1
                        ):
                            QMessageBox.warning(
                                self, "Chyba", "Trať už v databáze existuje"
                            )
                            self.parent.logger.error(
                                f"Route {new_route.route_name} already exists in database"
                            )
                            return

                        cur.execute(
                            f"INSERT INTO routes (uid, route_name) VALUES ('{str(new_route.uid)}', '{new_route.route_name}')"
                        )

                    for station, values in track["inflections"].items():
                        s = StationName()
                        s.station_name = station
                        s.station_name_N = values["nominative"]
                        s.station_name_G = values["genitive"]
                        s.station_name_L = values["local"]

                        with sqlite_handler.get_cursor() as cur:
                            cur.execute(
                                f"INSERT INTO station_names (station_name, station_name_N, station_name_G, station_name_L) VALUES ('{s.station_name}', '{s.station_name_N}', '{s.station_name_G}', '{s.station_name_L}')"
                            )

                    stations: list = []
                    for station, values in track["stations"].items():
                        s = Station()
                        s.uid = uuid4()  # regenerate uid each time
                        s.station_name = station
                        s.left_station = values["left_station"]
                        s.right_station = values["right_station"]
                        s.turn_station = values["turn_station"]
                        s.station_type = values["station_type"]
                        s.route_uid = new_route.uid
                        s.station_inflections = station
                        stations.append(s.__list__())

                    self.stations = pd.DataFrame(
                        columns=s.__dict__().keys(),
                        data=stations,
                    )
                    with sqlite_handler.get_connection() as conn:
                        self.stations.to_sql(
                            "stations", conn, if_exists="append", index=False
                        )

                except KeyError as e:
                    self.parent.logger.error(f"Error loading track file: {e}")
                    return

        self.fetch_data_from_db()

    def remove_track_func(self):
        pass
