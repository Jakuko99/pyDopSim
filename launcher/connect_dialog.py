import os
from PyQt5.QtWidgets import (
    QMainWindow,
    QLabel,
    QPushButton,
    QLineEdit,
    QMessageBox,
    QDialog,
    QListWidget,
    QComboBox,
)
from PyQt5.QtGui import QFont, QIntValidator
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

        self.server_ip = QLineEdit("localhost", self)
        self.server_ip.setFixedWidth(140)
        self.server_ip.setFont(self.font_obj)
        self.server_ip.move(70, 45)

        self.server_port_label = QLabel("Port:", self)
        self.server_port_label.setFont(self.font_obj)
        self.server_port_label.move(5, 80)

        self.server_port = QLineEdit("8020", self)
        self.server_port.setFont(self.font_obj)
        self.server_port.setFixedWidth(140)
        self.server_port.setValidator(QIntValidator(0, 65535))
        self.server_port.move(70, 80)

        self.connect_button = QPushButton("Pripojiť", self)
        self.connect_button.setFont(self.font_obj)
        self.connect_button.move(20, 215)
        self.connect_button.clicked.connect(self.connect_func)

        self.cancel_button = QPushButton("Zrušiť", self)
        self.cancel_button.setFont(self.font_obj)
        self.cancel_button.move(120, 215)
        self.cancel_button.clicked.connect(self.closeEvent)

        self.route_label = QLabel("Trať:", self)
        self.route_label.setFont(self.font_obj)
        self.route_label.move(5, 115)

        self.route_combo = QComboBox(self)
        self.route_combo.setFont(self.font_obj)
        self.route_combo.move(70, 115)
        self.route_combo.setFixedWidth(140)
        self.route_combo.setEnabled(False)

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
                    self.available_stations.addItem(station.get("station_name"))

        except requests.exceptions.ConnectionError:
            self.logger.error("Failed to get available stations, server not reachable")
            QMessageBox.critical(
                self,
                "Chyba pripojenia",
                f"Nepodarilo sa pripojiť k serveru na {self.server_ip.text()}:{self.server_port.text()}",
            )

        except requests.exceptions.InvalidURL:
            self.logger.error("Invalid URL entered")
            QMessageBox.critical(
                self,
                "Chyba URL",
                f"Zadaná URL adresa {self.server_ip.text()}:{self.server_port.text()} nie je platná",
            )

        except Exception as e:
            self.logger.error(f"Failed to get available stations: {e}")
            QMessageBox.critical(
                self,
                "Neznáma chyba",
                f"Nastala chyba pri získavaní dostupných staníc: {e}",
            )

    def closeEvent(self, event):
        self.logger.debug("Connect dialog dismissed")
        if not type(event) == bool:
            event.accept()
        else:
            self.close()

    def station_selected(self):
        selected_item: str = self.available_stations.currentItem().text()
        try:
            request = requests.put(
                f"http://{self.server_ip.text()}:{self.server_port.text()}/take_station/{selected_item}?client_name={self.player_name.text()}",
            )
            if request.status_code == 200:
                if "server_tcp_port" in request.json():
                    self.logger.info(f"Station {selected_item} taken")
                    self.on_confirm_callback(
                        self.server_ip.text(),
                        int(request.json().get("server_tcp_port")),
                        selected_item,
                        request.json(),
                    )  # call callback with selected station
                    self.close()

                elif "error" in request.json():
                    self.logger.error(f"Station {selected_item} already taken")
                    QMessageBox.critical(
                        self,
                        "Stanica už obsadená",
                        f"Stanica {selected_item} už je obsadená",
                    )
        except Exception as e:
            self.logger.error(f"Failed to take station: {e}")
            QMessageBox.critical(
                self,
                "Neznáma chyba",
                f"Nastala chyba pri pripájaní ku stanici: {e}",
            )
