import os
from PyQt5.QtWidgets import (
    QLabel,
    QPushButton,
    QComboBox,
    QLineEdit,
    QMessageBox,
    QMainWindow,
    QComboBox,
)
from PyQt5.QtGui import QFont, QIcon, QIntValidator
from PyQt5.QtCore import Qt
import os


class TelephoneDialog(QMainWindow):
    def __init__(self, parent= None):
        super().__init__(parent)
        self.font_obj = QFont("Arial", 10)
        self.setWindowTitle("Staničný telefón")
        self.setWindowIcon(QIcon("assets/phone_icon.png"))      
