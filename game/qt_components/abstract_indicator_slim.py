from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtCore import Qt, QTimer

from game.data_types.api_package import IndicatorState


class AbstractIndicatorSlim(QWidget):
    def __init__(self, indicator_color: str, parent=None):
        QWidget.__init__(self, parent=parent)
        self.color: str = indicator_color
        self.setGeometry(0, 0, 60, 60)
        self.state: IndicatorState = IndicatorState.OFF

        self.timer = QTimer(self)
        self.timer.timeout.connect(self._update)

        self.body = QLabel("", self)
        self.body.setGeometry(15, 0, 16, 16)
        self.body.setStyleSheet("background-color: gray; border-radius: 8px")

    def set_state(self, state: IndicatorState):  # TODO: finish ids
        self.timer.stop()

        if state == IndicatorState.ON:
            self.state = IndicatorState.ON
            self.body.setStyleSheet(
                f"background-color: {self.color}; border-radius: 8px"
            )
        elif state == IndicatorState.OFF:
            self.state = IndicatorState.OFF
            self.body.setStyleSheet(f"background-color: gray; border-radius: 8px")
        elif state == IndicatorState.BLINKING:
            self.timer.start(1000)
            self.state = IndicatorState.ON
            self.body.setStyleSheet(
                f"background-color: {self.color}; border-radius: 8px"
            )

    def _update(self):
        if self.state == IndicatorState.OFF:
            self.state = IndicatorState.ON
            self.body.setStyleSheet(
                f"background-color: {self.color}; border-radius: 8px"
            )
        else:
            self.state = IndicatorState.OFF
            self.body.setStyleSheet(f"background-color: gray; border-radius: 8px")
