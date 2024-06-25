import os
from PyQt5.QtWidgets import (
    QMainWindow,
    QLabel,
    QPushButton,
    QLineEdit,
    QMessageBox,
    QDialog,
    QListWidget,
)
from PyQt5.QtGui import QFont
import logging
import requests


class ConnectDialog(QDialog):
    def __init__(self, parent, on_confirm_callback=lambda x, y, z: None):
        super().__init__(parent)
        self.on_confirm_callback = on_confirm_callback
        self.font_obj = QFont("Arial", 11)

        self.logger = logging.getLogger("App.ConnectDialog")
        self.logger.setLevel(logging.DEBUG)

        self.setWindowTitle("Pripojiť ku serveru")
        self.setFixedSize(400, 250)

        self.player_label = QLabel("Meno:", self)
        self.player_label.setFont(self.font_obj)
        self.player_label.move(5, 10)

        self.player_name = QLineEdit(os.getlogin().capitalize(), self)
        self.player_name.setFixedWidth(140)
        self.player_name.setFont(self.font_obj)
        self.player_name.move(70, 10)

        self.server_label = QLabel("Server:", self)
        self.server_label.setFont(self.font_obj)
        self.server_label.move(5, 45)

        self.server_ip = QLineEdit(self)
        self.server_ip.setFixedWidth(140)
        self.server_ip.setFont(self.font_obj)
        self.server_ip.move(70, 45)

        self.server_port_label = QLabel("Port:", self)
        self.server_port_label.setFont(self.font_obj)
        self.server_port_label.move(5, 80)

        self.server_port = QLineEdit("8020", self)
        self.server_port.setFont(self.font_obj)
        self.server_port.setFixedWidth(140)
        self.server_port.move(70, 80)

        self.connect_button = QPushButton("Pripojiť", self)
        self.connect_button.setFont(self.font_obj)
        self.connect_button.move(20, 215)
        self.connect_button.clicked.connect(self.connect_func)

        self.cancel_button = QPushButton("Zrušiť", self)
        self.cancel_button.setFont(self.font_obj)
        self.cancel_button.move(120, 215)
        self.cancel_button.clicked.connect(self.closeEvent)

        self.available_stations = QListWidget(self)
        self.available_stations.setFont(self.font_obj)
        self.available_stations.move(230, 30)
        self.available_stations.setFixedSize(165, 215)
        self.available_stations.doubleClicked.connect(self.station_selected)

        self.available_stations_label = QLabel("Dostupné stanice:", self)
        self.available_stations_label.setFont(self.font_obj)
        self.available_stations_label.move(230, 5)

    def connect_func(self):
        self.logger.info(
            f"Trying to connect to server at {self.server_ip.text()}:{self.server_port.text()}"
        )
        try:
            request = requests.get(
                f"http://{self.server_ip.text()}:{self.server_port.text()}/available_stations"
            )
            if request.status_code == 200:
                self.available_stations.clear()
                for station in request.json():
                    self.available_stations.addItem(station)

        except requests.exceptions.ConnectionError:
            self.logger.error("Failed to get available stations")
            QMessageBox.critical(
                self,
                "Chyba pripojenia",
                f"Nepodarilo sa pripojiť k serveru na {self.server_ip.text()}:{self.server_port.text()}",
            )

    def closeEvent(self, event):
        self.logger.debug("Connect dialog dismissed")
        if not type(event) == bool:
            event.accept()
        else:
            self.close()

    def station_selected(self):
        selected_item: str = self.available_stations.currentItem().text()
        self.on_confirm_callback(
            self.server_ip.text(),
            int(self.server_port.text()),
            selected_item,
        )  # call callback with selected station
        self.close()
