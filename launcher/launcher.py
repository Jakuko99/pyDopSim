import logging
from PyQt5.QtWidgets import QLabel, QMainWindow, QTabWidget, QPushButton
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtCore import Qt
from queue import Queue

from client.api_package import Client
from game.tests.api_package import StationTest
from .game_info import GameInfo
from .game_tab import GameTab
from .settings_tab import SettingsTab
from .connect_dialog import ConnectDialog


class Launcher(QMainWindow):
    def __init__(self, log_pipe: Queue = None):
        super().__init__()
        self.log_pipe: Queue = log_pipe
        self.logger = logging.getLogger("App.Launcher")
        self.connect_dialog = ConnectDialog(self, self.run_client)

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
        self.game_tab.connect_button.clicked.connect(self.connect_to_server)
        self.tab_widget.addTab(self.game_tab, "Simulácia")

        self.settings_tab = SettingsTab(self)
        self.tab_widget.addTab(self.settings_tab, "Nastavenia")
        self.tab_widget.move(2, 336)

        self.exit_button = QPushButton("Ukončiť", self)
        self.exit_button.move(495, 565)
        self.exit_button.setFont(self._font)
        self.exit_button.clicked.connect(self.close)
        self.logger.info("pyDopSim Launcher started")

    def run_station_test(self):
        self.logger.debug("Running station test")
        self.station_test = StationTest(log_pipe=self.log_pipe)
        if not self.settings_tab.allow_2L_checkbox.isChecked():
            self.station_test.window.disable_2L_track()
            self.station_test.window.AHR_2L.setVisible(False)

        self.station_test.add_test_bindings()
        self.station_test.run()

    def run_client(self, host: str, port: int, station_name: str):
        self.client = Client(
            station_name=station_name,
            log_pipe=self.log_pipe,
            allow_debug=self.game_tab.allow_debug_checkbox.isChecked(),
        )
        self.client.set_server_info(host, port)
        self.client.connect()
        while (
            not self.client.connected
        ):  # wait for client to connect, maybe rework later
            self.client.run()

    def connect_to_server(self):
        self.logger.debug("Opening connect dialog")
        self.connect_dialog.show()
