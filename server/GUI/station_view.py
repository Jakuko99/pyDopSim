from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt


class StationView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(500, 268)
        self.setFont(QFont("Arial", 10))

        self.outline = QLabel(self)
        self.outline.setPixmap(QPixmap("assets/relief_siluette.png"))
        self.outline.move(0, 0)

        self._2L_label = QLabel("2L", self)
        self._2L_label.setWordWrap(True)
        self._2L_label.setFixedSize(90, 40)
        self._2L_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._2L_label.move(5, 35)

        self._1L_label = QLabel("1L", self)
        self._1L_label.setWordWrap(True)
        self._1L_label.setFixedSize(90, 40)
        self._1L_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._1L_label.move(5, 140)

        self._S_label = QLabel("S", self)
        self._S_label.setWordWrap(True)
        self._S_label.setFixedSize(90, 40)
        self._S_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._S_label.move(410, 140)

    def set_station_names(
        self, name_1L: str = None, name_2L: str = None, name_S: str = None
    ):
        self._1L_label.setText(name_1L if name_1L else "1L")
        self._2L_label.setText(name_2L if name_2L else "2L")
        self._S_label.setText(name_S if name_S else "S")
