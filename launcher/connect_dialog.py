import os
from PyQt5.QtWidgets import (
    QMainWindow,
    QLabel,
    QPushButton,
    QLineEdit,
    QMessageBox,
    QListView,
    QDialog,
)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
import logging


class ConnectDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.font_obj = QFont("Arial", 11)

        self.logger = logging.getLogger("App.ConnectDialog")
        self.logger.setLevel(logging.DEBUG)

        self.setWindowTitle("Pripojiť ku serveru")
        self.setFixedSize(400, 250)

        self.player_label = QLabel("Meno:", self)
        self.player_label.setFont(self.font_obj)
        self.player_label.move(5, 10)

        self.player_name = QLineEdit(os.getlogin().capitalize(), self)
        self.player_name.setFont(self.font_obj)
        self.player_name.move(70, 10)

        self.server_label = QLabel("Server:", self)
        self.server_label.setFont(self.font_obj)
        self.server_label.move(5, 45)

        self.server_ip = QLineEdit(self)
        self.server_ip.setFont(self.font_obj)
        self.server_ip.move(70, 45)

        self.server_port_label = QLabel("Port:", self)
        self.server_port_label.setFont(self.font_obj)
        self.server_port_label.move(5, 80)

        self.server_port = QLineEdit("8000", self)
        self.server_port.setFont(self.font_obj)
        self.server_port.move(70, 80)

        self.connect_button = QPushButton("Pripojiť", self)
        self.connect_button.setFont(self.font_obj)
        self.connect_button.move(30, 215)
        self.connect_button.clicked.connect(self.connect_func)

        self.cancel_button = QPushButton("Zrušiť", self)
        self.cancel_button.setFont(self.font_obj)
        self.cancel_button.move(130, 215)
        self.cancel_button.clicked.connect(self.close_func)

        self.available_stations = QListView(self)
        self.available_stations.move(250, 30)
        self.available_stations.resize(145, 215)
        self.available_stations.clicked.connect(self.station_selected)

        self.available_stations_label = QLabel("Dostupné stanice:", self)
        self.available_stations_label.setFont(self.font_obj)
        self.available_stations_label.move(250, 5)

    def connect_func(self):
        self.logger.info(
            f"Trying to connect to server at {self.server_ip.text()}:{self.server_port.text()}"
        )

    def close_func(self):
        self.logger.info("Connection to server aborted")
        self.close()

    def station_selected(self):
        pass
