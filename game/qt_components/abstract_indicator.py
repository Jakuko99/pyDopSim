from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QTimer

from game.data_types.api_package import IndicatorState


class AbstractIndicator(QWidget):
    def __init__(self, indicator_color: str, text: str, parent=None):
        QWidget.__init__(self, parent=parent)
        self.color: str = indicator_color
        self.setGeometry(0, 0, 60, 60)
        self.state: IndicatorState = IndicatorState.OFF

        self.timer = QTimer(self)
        self.timer.timeout.connect(self._update)

        self.body = QLabel("", self)
        self.body.setGeometry(15, 0, 22, 22)
        self.body.setStyleSheet(
            "border: 4px solid black; background-color: gray; border-radius: 11px"
        )

        self.label = QLabel(text, self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setFont(QFont("Arial", 10))
        self.label.setStyleSheet("background-color: white; color: black;")
        self.label.move(0, 23)

    def set_state(self, state: IndicatorState):  # TODO: finish ids
        self.timer.stop()

        if state == IndicatorState.ON:
            self.state = IndicatorState.ON
            self.body.setStyleSheet(
                f"border: 4px solid black; background-color: {self.color}; border-radius: 11px"
            )
        elif state == IndicatorState.OFF:
            self.state = IndicatorState.OFF
            self.body.setStyleSheet(
                f"border: 4px solid black; background-color: gray; border-radius: 11px"
            )
        elif state == IndicatorState.BLINKING:
            self.timer.start(1000)
            self.state = IndicatorState.ON
            self.body.setStyleSheet(
                f"border: 4px solid black; background-color: {self.color}; border-radius: 11px"
            )

    def _update(self):
        if self.state == IndicatorState.OFF:
            self.state = IndicatorState.ON
            self.body.setStyleSheet(
                f"border: 4px solid black; background-color: {self.color}; border-radius: 11px"
            )
        else:
            self.state = IndicatorState.OFF
            self.body.setStyleSheet(
                f"border: 4px solid black; background-color: gray; border-radius: 11px"
            )
