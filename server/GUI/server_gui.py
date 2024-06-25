from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon

from server.rest_server.api_package import RESTServer
from server.tcp_server.api_package import TCPServer
import server.data_types.api_package as data_types


class ServerGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyDopSim Server")
        self.setWindowIcon(QIcon("assets/app_icon.png"))
        self.setFixedSize(600, 600)
