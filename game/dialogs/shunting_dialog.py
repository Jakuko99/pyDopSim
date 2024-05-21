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
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtCore import Qt
import os


class ShuntingDialog(QMainWindow):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.font_obj = QFont("Arial", 10)
        self.setWindowTitle("Posun súpravy")
        self.setWindowIcon(QIcon("assets/shunting_icon.png"))
        self._parent = parent

        self.lab = QLabel(self)
        self.lab.setText(str(self._parent.uuid))  # access info about consist
        # self.setFixedSize(630, 365)
