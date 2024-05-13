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


class ConnectDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.font_obj = QFont("Arial", 11)

        self.setWindowTitle("Pripojiť k serveru")
        self.setFixedSize(275, 150)

        self.player_label = QLabel("Meno:", self)
        self.player_label.setFont(self.font_obj)
        self.player_label.move(10, 10)

        self.player_name = QLineEdit(os.getlogin(), self)
        self.player_name.setFont(self.font_obj)
        self.player_name.move(75, 10)

        self.server_label = QLabel("Server:", self)
        self.server_label.setFont(self.font_obj)
        self.server_label.move(10, 45)

        self.server_ip = QLineEdit(self)
        self.server_ip.setFont(self.font_obj)
        self.server_ip.move(75, 45)

        self.server_port_label = QLabel("Port:", self)
        self.server_port_label.setFont(self.font_obj)
        self.server_port_label.move(10, 80)

        self.server_port = QLineEdit("8000", self)
        self.server_port.setFont(self.font_obj)
        self.server_port.move(75, 80)

        self.connect_button = QPushButton("Pripojiť", self)
        self.connect_button.setFont(self.font_obj)
        self.connect_button.move(80, 115)
        self.connect_button.clicked.connect(self.connect_func)

        self.cancel_button = QPushButton("Zrušiť", self)
        self.cancel_button.setFont(self.font_obj)
        self.cancel_button.move(180, 115)
        self.cancel_button.clicked.connect(self.close)

    def connect_func(self):
        pass
