import os
from PyQt5.QtWidgets import (
    QMainWindow,
    QLabel,
    QPushButton,
    QComboBox,
    QLineEdit,
    QMessageBox,
    QMenu,
    QAction,
    QDialog,
)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
import logging


class DebugDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.font_obj = QFont("Arial", 11)

        self.logger = logging.getLogger("App.DebugDialog")
        self.logger.setLevel(logging.DEBUG)
        self.logger.debug("Debug Dialog created")

        self.setWindowTitle("Debug Window")
