from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QComboBox
from PyQt5.QtGui import QFont


class GameTab(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self._font = QFont("Arial", 10)

        self.test_station_button = QPushButton("Test stanice", self)
        self.test_station_button.move(200, 10)
        self.test_station_button.setFixedSize(200, 25)
        self.test_station_button.setFont(self._font)

        self.connect_button = QPushButton("Pripojit ku serveru", self)
        self.connect_button.move(200, 40)
        self.connect_button.setFixedSize(200, 25)
        self.connect_button.setFont(self._font)
