from PyQt5.QtWidgets import QWidget, QLabel, QPushButton
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt

from game.data_types.api_package import LeverState


class AbstractLeverSlim(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.setGeometry(0, 0, 60, 120)
        self.state: LeverState = LeverState.MIDDLE
        self.on_update = lambda state: None

        self.lever_middle_pixmap = QPixmap("assets/lever_middle.png")
        self.lever_left_pixmap = QPixmap("assets/lever_left.png")
        self.lever_right_pixmap = QPixmap("assets/lever_right.png")

        self.body = QLabel("", self)
        self.body.setGeometry(0, 0, 60, 110)

        self.light1 = QLabel("", self)
        self.light1.setGeometry(5, 15, 20, 20)
        self.light1.setStyleSheet(
            "background-color: gray; border-radius: 10px; border: 4px solid black;"
        )
        self.light2 = QLabel("", self)
        self.light2.setGeometry(20, 0, 20, 20)
        self.light2.setStyleSheet(
            "background-color: gray; border-radius: 10px; border: 4px solid black;"
        )
        self.light3 = QLabel("", self)
        self.light3.setGeometry(35, 15, 20, 20)
        self.light3.setStyleSheet(
            "background-color: gray; border-radius: 10px; border: 4px solid black;"
        )

        self.lever = QLabel("", self)
        self.lever.setGeometry(0, 60, 60, 50)
        self.lever.setPixmap(self.lever_middle_pixmap)
        self.lever.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.area1 = QPushButton("", self)
        self.area1.setGeometry(0, 60, 20, 110)
        self.area1.setStyleSheet("background-color: transparent; border: none;")
        self.area1.clicked.connect(lambda: self._set_state(LeverState.LEFT))

        self.area2 = QPushButton("", self)
        self.area2.setGeometry(20, 60, 20, 110)
        self.area2.setStyleSheet("background-color: transparent; border: none;")
        self.area2.clicked.connect(lambda: self._set_state(LeverState.MIDDLE))

        self.area3 = QPushButton("", self)
        self.area3.setGeometry(40, 60, 20, 110)
        self.area3.setStyleSheet("background-color: transparent; border: none;")
        self.area3.clicked.connect(lambda: self._set_state(LeverState.RIGHT))

    def set_update_function(self, function):
        self.on_update = function

    def _set_state(self, state: LeverState):
        self.state = state
        self.on_update(state)  # call function on update

        if state == LeverState.LEFT:
            self.lever.setPixmap(self.lever_left_pixmap)
        elif state == LeverState.MIDDLE:
            self.lever.setPixmap(self.lever_middle_pixmap)
        elif state == LeverState.RIGHT:
            self.lever.setPixmap(self.lever_right_pixmap)

    def set_light(self, light_id: int, color: str):
        for i in range(1, 4):
            self.__getattribute__(f"light{i}").setStyleSheet(
                "background-color: gray; border-radius: 10px; border: 4px solid black;"
            )

        light: QLabel = self.__getattribute__(f"light{light_id}")
        light.setStyleSheet(
            f"background-color: {color}; border-radius: 10px; border: 4px solid black;"
        )
