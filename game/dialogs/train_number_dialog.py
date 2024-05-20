import os
from PyQt5.QtWidgets import (
    QLabel,
    QPushButton,
    QComboBox,
    QLineEdit,
    QMessageBox,
    QDialog,
    QMainWindow,
    QComboBox,
    QListWidget,
    QScrollArea,
    QCheckBox,
)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
import os


class TrainNumberDialog(QMainWindow):
    def __init__(self, parent):
        super().__init__(parent)
        self.font_obj = QFont("Arial", 10)
        self.setWindowTitle("Zaviest nový vlak")
        # self.setFixedSize(630, 365)
