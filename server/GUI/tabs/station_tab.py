from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QComboBox,
    QCheckBox,
    QLineEdit,
)
from PyQt5.QtGui import QFont, QIntValidator


class StationTab(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self._font = QFont("Arial", 10)

        self.station_name_label = QLabel("Názov stanice:", self)
        self.station_name_label.move(5, 5)
        self.station_name_label.setFont(self._font)

        self.station_name_input = QLineEdit(self)
        self.station_name_input.move(140, 5)
        self.station_name_input.setFont(self._font)
