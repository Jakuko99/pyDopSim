from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QComboBox,
    QCheckBox,
    QLineEdit,
)
from PyQt5.QtGui import QFont, QIntValidator


class ConfigTab(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self._font = QFont("Arial", 10)

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

        self.clear_db_button = QPushButton("Vymazať databázu", self)
        self.clear_db_button.move(5, 75)
        self.clear_db_button.setFont(self._font)
        self.clear_db_button.setFixedWidth(150)
