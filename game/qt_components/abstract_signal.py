from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtCore import QTimer

from game.data_types.api_package import SignalSign


class AbstractSignal(QWidget):
    def __init__(self, num_lamps: int, parent=None):
        QWidget.__init__(self, parent)
        self.setGeometry(0, 0, 30, (num_lamps * 15) + 5)
        self.num_lamps = num_lamps
        self.lamps: list[QLabel] = []

        self.background = QLabel(self)
        self.background.setGeometry(0, 0, 20, (num_lamps * 15) + 5)
        self.background.setStyleSheet("background-color: black")

        if num_lamps == 5:
            self.stripe1 = QLabel(self)
            self.stripe1.setGeometry(20, 0, 8, ((num_lamps * 15) + 5) * 0.4)
            self.stripe1.setStyleSheet("background-color: red")
            self.stripe2 = QLabel(self)
            self.stripe2.setGeometry(
                20, ((num_lamps * 15) + 5) * 0.4, 8, ((num_lamps * 15) + 5) * 0.2
            )
            self.stripe2.setStyleSheet("background-color: white")
            self.stripe3 = QLabel(self)
            self.stripe3.setGeometry(
                20, ((num_lamps * 15) + 5) * 0.6, 8, ((num_lamps * 15) + 5) * 0.4
            )
            self.stripe3.setStyleSheet("background-color: red")

        self.timer = QTimer(self)
        self.timer.timeout.connect(self._update)
        self.blinking_lamp: list = None
        self.lamp_state: bool = True

        for i in range(num_lamps):
            label = QLabel(self)
            label.setGeometry(5, (i * 15) + 5, 10, 10)
            label.setStyleSheet("background-color: black; border-radius: 5px;")
            self.lamps.append(label)

        if self.num_lamps == 5:  # default sign setting
            self.set_sign(SignalSign.STOP)
        elif self.num_lamps == 2:
            self.set_sign(SignalSign.SHUNT_PROHIBITED)
        elif self.num_lamps == 3:
            self.set_sign(SignalSign.AB_STOP)

        # self.lamps[0].setStyleSheet("background-color: yellow; border-radius: 5px;")
        # self.lamps[1].setStyleSheet("background-color: lime; border-radius: 5px;")
        # self.lamps[2].setStyleSheet("background-color: red; border-radius: 5px;")
        # self.lamps[3].setStyleSheet("background-color: white; border-radius: 5px;")
        # self.lamps[4].setStyleSheet("background-color: yellow; border-radius: 5px;")

    def set_sign(self, sign: SignalSign):
        for lamp in self.lamps:  # reset all lamps
            lamp.setStyleSheet("background-color: black; border-radius: 5px;")
        self.timer.stop()

        if self.num_lamps == 5:
            if sign == SignalSign.FREE:
                self.lamps[1].setStyleSheet(
                    "background-color: lime; border-radius: 5px;"
                )
            elif sign == SignalSign.STOP:
                self.lamps[2].setStyleSheet(
                    "background-color: red; border-radius: 5px;"
                )
            elif sign == SignalSign.SUMMON:
                self.lamps[2].setStyleSheet(
                    "background-color: red; border-radius: 5px;"
                )
                self.lamps[3].setStyleSheet(
                    "background-color: white; border-radius: 5px;"
                )
                self.timer.start(500)
                self.blinking_lamp = [self.lamps[3], "white"]
            elif sign == SignalSign.WARN:
                self.lamps[0].setStyleSheet(
                    "background-color: yellow; border-radius: 5px;"
                )
            elif sign == SignalSign.EXP40:
                self.lamps[0].setStyleSheet(
                    "background-color: yellow; border-radius: 5px;"
                )
                self.timer.start(500)
                self.blinking_lamp = [self.lamps[0], "yellow"]
            elif sign == SignalSign.EXP60:
                self.lamps[0].setStyleSheet(
                    "background-color: yellow; border-radius: 5px;"
                )
                self.timer.start(250)
                self.blinking_lamp = [self.lamps[0], "yellow"]
            elif sign == SignalSign.EXP80:
                self.lamps[1].setStyleSheet(
                    "background-color: lime; border-radius: 5px;"
                )
                self.timer.start(500)
                self.blinking_lamp = [self.lamps[1], "lime"]
            elif sign == SignalSign.SDP40_FREE:
                self.lamps[1].setStyleSheet(
                    "background-color: lime; border-radius: 5px;"
                )
                self.lamps[4].setStyleSheet(
                    "background-color: yellow; border-radius: 5px;"
                )
            elif sign == SignalSign.WARN_40:
                self.lamps[0].setStyleSheet(
                    "background-color: yellow; border-radius: 5px;"
                )
                self.lamps[4].setStyleSheet(
                    "background-color: yellow; border-radius: 5px;"
                )
            elif sign == SignalSign.SHUNT:
                self.lamps[3].setStyleSheet(
                    "background-color: white; border-radius: 5px;"
                )
            elif sign == SignalSign.EXP40_40:  # blinking yellow
                self.lamps[0].setStyleSheet(
                    "background-color: yellow; border-radius: 5px;"
                )
                self.lamps[4].setStyleSheet(
                    "background-color: yellow; border-radius: 5px;"
                )
                self.timer.start(500)
                self.blinking_lamp = [self.lamps[0], "yellow"]
            elif sign == SignalSign.EXP40_60:
                self.lamps[0].setStyleSheet(
                    "background-color: yellow; border-radius: 5px;"
                )
                self.lamps[4].setStyleSheet(
                    "background-color: yellow; border-radius: 5px;"
                )
                self.timer.start(250)
                self.blinking_lamp = [self.lamps[0], "yellow"]
            else:  # invalid state
                self.lamps[2].setStyleSheet(
                    "background-color: red; border-radius: 5px;"
                )

        elif self.num_lamps == 2:
            if sign == SignalSign.SHUNT_PROHIBITED:
                self.lamps[1].setStyleSheet(
                    "background-color: #1799E7; border-radius: 5px;"
                )
            elif sign == SignalSign.SHUNT:
                self.lamps[0].setStyleSheet(
                    "background-color: white; border-radius: 5px;"
                )
            else:
                self.lamps[1].setStyleSheet(
                    "background-color: #1799E7; border-radius: 5px;"
                )

        elif self.num_lamps == 3:
            if sign == SignalSign.AB_FREE:
                self.lamps[1].setStyleSheet(
                    "background-color: lime; border-radius: 5px;"
                )
            elif sign == SignalSign.AB_STOP:
                self.lamps[2].setStyleSheet(
                    "background-color: red; border-radius: 5px;"
                )
            elif sign == SignalSign.AB_WARN:
                self.lamps[0].setStyleSheet(
                    "background-color: yellow; border-radius: 5px;"
                )
            elif sign == SignalSign.AB_EXP40:
                self.lamps[0].setStyleSheet(
                    "background-color: yellow; border-radius: 5px;"
                )
                self.timer.start(500)
                self.blinking_lamp = [self.lamps[0], "yellow"]
            elif sign == SignalSign.AB_EXP60:
                self.lamps[0].setStyleSheet(
                    "background-color: yellow; border-radius: 5px;"
                )
                self.timer.start(250)
                self.blinking_lamp = [self.lamps[0], "yellow"]
            elif sign == SignalSign.AB_EXP80:
                self.lamps[1].setStyleSheet(
                    "background-color: lime; border-radius: 5px;"
                )
                self.timer.start(500)
                self.blinking_lamp = [self.lamps[1], "lime"]
            else:
                self.lamps[2].setStyleSheet(
                    "background-color: red; border-radius: 5px;"
                )

    def _update(self):
        if self.lamp_state:
            self.blinking_lamp[0].setStyleSheet(
                f"background-color: black; border-radius: 5px;"
            )
        else:
            self.blinking_lamp[0].setStyleSheet(
                f"background-color: {self.blinking_lamp[1]}; border-radius: 5px;"
            )
        self.lamp_state = not self.lamp_state  # invert state
