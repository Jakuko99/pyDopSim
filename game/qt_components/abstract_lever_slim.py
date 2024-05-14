from PyQt5.QtWidgets import QWidget, QLabel, QPushButton
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt

from game.data_types.api_package import LeverState, IndicatorColor, IndicatorState
from game.qt_components.abstract_switch_indicator import AbstractSwitchIndicator


class AbstractLeverSlim(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.setGeometry(0, 0, 65, 120)
        self.state: LeverState = LeverState.MIDDLE
        self.on_update = lambda state: None

        self.lever_middle_pixmap = QPixmap("assets/lever_middle.png")
        self.lever_left_pixmap = QPixmap("assets/lever_left.png")
        self.lever_right_pixmap = QPixmap("assets/lever_right.png")

        self.light1 = AbstractSwitchIndicator(IndicatorColor.GREEN, self)
        self.light1.move(0, 15)

        self.light2 = AbstractSwitchIndicator(IndicatorColor.RED, self)
        self.light2.move(20, 0)

        self.light3 = AbstractSwitchIndicator(IndicatorColor.YELLOW, self)
        self.light3.move(40, 15)

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

    def set_light(self, light_id: int, state: IndicatorState):
        for i in range(1, 4):  # reset lights
            self.__getattribute__(f"light{i}").set_state(IndicatorState.OFF)
        light: AbstractSwitchIndicator = self.__getattribute__(f"light{light_id}")
        light.set_state(state)
