from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit, QLabel, QTabWidget
from PyQt5.QtGui import QIcon, QIntValidator, QFont
import logging

from server.py_dop_sim_server import PyDopSimServer
import server.data_types.api_package as data_types
from .tabs import api_package as tabs


class ServerGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyDopSim Server")
        self.setWindowIcon(QIcon("assets/app_icon.png"))
        self.setFixedSize(600, 600)
        self._font = QFont("Arial", 12)

        self.logger = logging.getLogger("App.Server.GUI")
        self.logger.setLevel(logging.DEBUG)

        self.server: PyDopSimServer = PyDopSimServer()
        self.tab_view = QTabWidget(self)
        self.tab_view.setFixedSize(600, 565)
        self.tab_view.move(0, 0)

        self.station_tab = tabs.StationTab(self)
        self.tab_view.addTab(self.station_tab, "Stanice")

        self.overview_tab = tabs.OverviewTab(self)
        self.tab_view.addTab(self.overview_tab, "Prehľad")

        self.config_tab = tabs.ConfigTab(self)
        self.tab_view.addTab(self.config_tab, "Nastavenia servera")

        self.start_button = QPushButton("Spustiť server", self)
        self.start_button.move(5, 567)
        self.start_button.setFixedSize(590, 30)
        self.start_button.setFont(self._font)
        self.start_button.clicked.connect(self.start_server)

    def start_server(self):
        if self.server.running:
            self.server.stop()
            self.start_button.setText("Spustiť server")
        else:
            self.server.set_ports(
                rest_port=int(self.config_tab.rest_port_input.text()),
                tcp_port=int(self.config_tab.tcp_port_input.text()),
            )
            self.server.rest.stations["Vrútky"] = data_types.StationStatus.OFFLINE
            self.server.rest.stations["Žilina"] = data_types.StationStatus.OFFLINE
            self.start_button.setText("Zastaviť server")
            self.server.run()
