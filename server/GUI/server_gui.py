from PyQt5.QtWidgets import (
    QMainWindow,
    QPushButton,
    QLineEdit,
    QLabel,
    QTabWidget,
    QMessageBox,
)
from PyQt5.QtGui import QIcon, QIntValidator, QFont
import logging

from server.py_dop_sim_server import PyDopSimServer
import server.data_types.api_package as data_types
from .tabs import api_package as tabs
from utils.api_package import sqlite_handler


class ServerGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyDopSim Server")
        self.setWindowIcon(QIcon("assets/app_icon.png"))
        self.setFixedSize(600, 600)
        self._font = QFont("Arial", 12)

        self.logger = logging.getLogger("App.Server.GUI")
        self.logger.setLevel(logging.DEBUG)

        self.server: PyDopSimServer = PyDopSimServer()
        self.tab_view = QTabWidget(self)
        self.tab_view.setFixedSize(600, 565)
        self.tab_view.move(0, 0)

        self.station_tab = tabs.StationTab(self)
        self.tab_view.addTab(self.station_tab, "Stanice")

        self.creator_tab = tabs.CreatorTab(self)
        self.tab_view.addTab(self.creator_tab, "Vytvorenie trate")

        self.overview_tab = tabs.OverviewTab(self)
        self.tab_view.addTab(self.overview_tab, "Prehľad")

        self.config_tab = tabs.ConfigTab(self)
        self.tab_view.addTab(self.config_tab, "Nastavenia servera")
        self.config_tab.clear_db_button.clicked.connect(self.clear_db)
        self.config_tab.delete_trains_button.clicked.connect(self.delete_trains)

        self.start_button = QPushButton("Spustiť server", self)
        self.start_button.move(5, 567)
        self.start_button.setFixedSize(590, 30)
        self.start_button.setFont(self._font)
        self.start_button.clicked.connect(self.start_server)

    def start_server(self):
        if self.server.running:
            self.server.stop()
            self.start_button.setText("Spustiť server")
        else:
            self.server.set_ports(
                rest_port=int(self.config_tab.rest_port_input.text()),
                tcp_port=int(self.config_tab.tcp_port_input.text()),
            )

            self.server.add_station_dict(self.station_tab.stations)

            self.start_button.setText("Zastaviť server")
            self.server.run()

    def clear_db(self):
        question_box = QMessageBox.question(
            self,
            "Vymazanie databázy",
            "Naozaj chcete vymazať obsah databázy?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )
        if question_box == QMessageBox.Yes:
            with sqlite_handler.get_cursor() as cursor:
                cursor.execute("DELETE FROM stations")
                cursor.execute("DELETE FROM trains")
                cursor.execute("DELETE FROM station_names")
                cursor.execute("DELETE FROM routes")

            self.station_tab.fetch_data_from_db()
            self.logger.info("Database cleared")

    def delete_trains(self):
        question_box = QMessageBox.question(
            self,
            "Vymazanie vlakov",
            "Naozaj chcete odstrániť všetky vlaky?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )
        if question_box == QMessageBox.Yes:
            with sqlite_handler.get_cursor() as cursor:
                cursor.execute("DELETE FROM trains")

            self.logger.info("Trains deleted")
