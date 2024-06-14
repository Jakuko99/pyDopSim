from PyQt5.QtWidgets import QLabel, QMainWindow, QTabWidget, QPushButton, QWidget
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtCore import Qt

from client.api_package import Client
from game.tests.api_package import StationTest
from .game_info import GameInfo
from .game_tab import GameTab
from .settings_tab import SettingsTab


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

        self.tab_widget = QTabWidget(self)
        self.tab_widget.resize(598, 225)
        self.tab_widget.setFont(self._font)

        self.game_tab = GameTab(self)
        self.game_tab.test_station_button.clicked.connect(self.run_station_test)
        self.tab_widget.addTab(self.game_tab, "Hra")

        self.settings_tab = SettingsTab(self)
        self.tab_widget.addTab(self.settings_tab, "Nastavenia")
        self.tab_widget.move(2, 336)

        self.exit_button = QPushButton("Ukončiť", self)
        self.exit_button.move(495, 565)
        self.exit_button.setFont(self._font)
        self.exit_button.clicked.connect(self.close)

    def run_station_test(self):
        self.station_test = StationTest()
        self.station_test.add_test_bindings()
        self.station_test.run()
