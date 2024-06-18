from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QComboBox, QCheckBox
from PyQt5.QtGui import QFont


class GameTab(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self._font = QFont("Arial", 10)

        self.connect_button = QPushButton("Pripojiť ku serveru", self)
        self.connect_button.move(200, 10)
        self.connect_button.setFixedSize(200, 25)
        self.connect_button.setFont(self._font)

        self.log_button = QPushButton("Zobraziť log", self)
        self.log_button.move(200, 40)
        self.log_button.setFixedSize(200, 25)
        self.log_button.setFont(self._font)

        self.test_station_button = QPushButton("Test stanice", self)
        self.test_station_button.move(200, 70)
        self.test_station_button.setFixedSize(200, 25)
        self.test_station_button.setFont(self._font)

        self.allow_debug_checkbox = QCheckBox("Povoliť debug", self)
        self.allow_debug_checkbox.setFont(self._font)
        self.allow_debug_checkbox.move(465, 170)
