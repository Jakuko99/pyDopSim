from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QComboBox, QCheckBox
from PyQt5.QtGui import QFont


class GameTab(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.setFont(QFont("Arial", 11))  # set font globally

        self.connect_button = QPushButton("Pripojiť ku serveru", self)
        self.connect_button.move(200, 5)
        self.connect_button.setFixedSize(200, 30)

        self.start_server_button = QPushButton("Spustiť server", self)
        self.start_server_button.move(200, 40)
        self.start_server_button.setFixedSize(200, 30)

        self.dispatcher_button = QPushButton("Dispečerská aplikácia", self)
        self.dispatcher_button.move(200, 75)
        self.dispatcher_button.setFixedSize(200, 30)

        self.log_button = QPushButton("Zobraziť log", self)
        self.log_button.move(200, 110)
        self.log_button.setFixedSize(200, 30)

        self.test_station_button = QPushButton("Test stanice", self)
        self.test_station_button.move(200, 145)
        self.test_station_button.setFixedSize(200, 30)

        self.allow_debug_checkbox = QCheckBox("Povoliť debug", self)
        self.allow_debug_checkbox.move(455, 165)
