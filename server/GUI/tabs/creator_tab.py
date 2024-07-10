from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QComboBox,
    QCheckBox,
    QLineEdit,
    QFileDialog,
)
from PyQt5.QtGui import QFont

from ..station_view import StationView


class CreatorTab(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.setFont(QFont("Arial", 11))

        self.route_name_label = QLabel("Názov trate:", self)
        self.route_name_label.move(5, 10)

        self.route_name_input = QLineEdit(self)
        self.route_name_input.move(110, 5)
        self.route_name_input.setFixedSize(150, 30)
