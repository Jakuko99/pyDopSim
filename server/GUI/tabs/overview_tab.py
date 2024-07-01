from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QComboBox,
    QCheckBox,
    QLineEdit,
)
from PyQt5.QtGui import QFont, QIntValidator


class OverviewTab(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.setFont(QFont("Arial", 11))  # set font globally
