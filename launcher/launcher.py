from PyQt5.QtWidgets import QLabel, QMainWindow, QTableView, QPushButton
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtCore import Qt

from client.api_package import Client
from game.tests.api_package import StationTest
from .game_info import GameInfo


class Launcher(QMainWindow):
    def __init__(self, allow_debug_mode: bool = False):
        super().__init__()
        self.allow_debug_mode = allow_debug_mode
        self.setWindowIcon(QIcon("assets/app_icon.png"))
        self.setWindowTitle("PyDopSim Launcher")
        self.setFixedSize(600, 600)
        self._font = QFont("Arial", 10)

        self.cover = QLabel(self)
        self.cover.setPixmap(QPixmap("assets/menu_photo.png"))
        self.cover.move(0, 0)
        self.cover.setScaledContents(True)
        self.cover.resize(600, 336)

        self.version_label = QLabel(f"**Verzia:** {GameInfo.VERSION}", self)
        self.version_label.move(250, 336)
        self.version_label.setTextFormat(Qt.TextFormat.MarkdownText)
        self.version_label.setFont(self._font)

        self.exit_button = QPushButton("Ukončiť", self)
        self.exit_button.move(495, 565)
        self.exit_button.setFont(self._font)
        self.exit_button.clicked.connect(self.close)
