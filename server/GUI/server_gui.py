from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QIcon, QIntValidator, QFont

from server.py_dop_sim_server import PyDopSimServer
import server.data_types.api_package as data_types


class ServerGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyDopSim Server")
        self.setWindowIcon(QIcon("assets/app_icon.png"))
        self.setFixedSize(600, 600)
        self._font = QFont("Arial", 10)

        self.server: PyDopSimServer = PyDopSimServer()

        self.rest_port_label = QLabel("REST port:", self)
        self.rest_port_label.setFont(self._font)
        self.rest_port_label.move(5, 5)

        self.rest_port_input = QLineEdit(self)
        self.rest_port_input.move(90, 5)
        self.rest_port_input.setValidator(QIntValidator(0, 65535))
        self.rest_port_input.setFont(self._font)
        self.rest_port_input.setText("8020")

        self.tcp_port_label = QLabel("TCP port:", self)
        self.tcp_port_label.setFont(self._font)
        self.tcp_port_label.move(15, 40)

        self.tcp_port_input = QLineEdit(self)
        self.tcp_port_input.move(90, 40)
        self.tcp_port_input.setValidator(QIntValidator(0, 65535))
        self.tcp_port_input.setFont(self._font)
        self.tcp_port_input.setText("8021")
