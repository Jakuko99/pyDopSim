from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit, QLabel, QTabWidget
from PyQt5.QtGui import QIcon, QIntValidator, QFont

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

        self.server: PyDopSimServer = PyDopSimServer()
        self.tab_view = QTabWidget(self)
        self.tab_view.setFixedSize(600, 565)
        self.tab_view.move(0, 0)

        self.station_tab = tabs.StationTab(self)
        self.tab_view.addTab(self.station_tab, "Stanice")

        self.config_tab = tabs.ConfigTab(self)
        self.tab_view.addTab(self.config_tab, "Nastavenia servera")

        self.start_button = QPushButton("Spustiť server", self)
        self.start_button.move(5, 567)
        self.start_button.setFixedSize(590, 30)
        self.start_button.setFont(self._font)
        self.start_button.clicked.connect(self.start_server)

    def start_server(self):
        self.server.set_ports(
            rest_port=int(self.config_tab.rest_port_input.text()),
            tcp_port=int(self.config_tab.tcp_port_input.text()),
        )
        self.server.rest.stations["Vrakuna"] = data_types.StationStatus.OFFLINE
        self.server.rest.stations["Ruzinov"] = data_types.StationStatus.OFFLINE
        self.server.run()
