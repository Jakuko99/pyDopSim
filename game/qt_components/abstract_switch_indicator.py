from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap

from game.data_types.api_package import IndicatorState, IndicatorColor


class AbstractSwitchIndicator(QWidget):
    def __init__(self, indicator_color: IndicatorColor, parent=None):
        QWidget.__init__(self, parent=parent)
        self.color: str = indicator_color
        self.setGeometry(0, 0, 25, 25)
        self.state: IndicatorState = IndicatorState.OFF
        self.off_pixmap = QPixmap("assets/switch_indicator_off.png")
        self.on_pixmap = QPixmap(
            f"assets/switch_indicator_on_{indicator_color.name.lower()}.png"
        )

        self.timer = QTimer(self)
        self.timer.timeout.connect(self._update)

        self.body = QLabel("", self)
        self.body.setGeometry(0, 0, 25, 25)
        self.body.setScaledContents(True)
        self.body.setPixmap(self.off_pixmap)
        self.body.setStyleSheet("background-color: transparent;")

    def set_state(self, state: IndicatorState):  # TODO: finish ids
        self.timer.stop()

        if state == IndicatorState.ON:
            self.state = IndicatorState.ON
            self.body.setPixmap(self.on_pixmap)
        elif state == IndicatorState.OFF:
            self.state = IndicatorState.OFF
            self.body.setPixmap(self.off_pixmap)
        elif state == IndicatorState.BLINKING:
            self.timer.start(1000)
            self.state = IndicatorState.ON
            self.body.setPixmap(self.on_pixmap)

    def _update(self):
        if self.state == IndicatorState.OFF:
            self.state = IndicatorState.ON
            self.body.setPixmap(self.on_pixmap)
        else:
            self.state = IndicatorState.OFF
            self.body.setPixmap(self.off_pixmap)
