from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QComboBox


class SettingsTab(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.station_label = QLabel("Stanica:", self)
        self.station_label.move(10, 10)

        self.station_combobox = QComboBox(self)
        self.station_combobox.move(10, 30)
        self.station_combobox.resize(200, 30)

        self.start_button = QPushButton("Spustiť", self)
        self.start_button.move(10, 70)
        self.start_button.resize(200, 30)
