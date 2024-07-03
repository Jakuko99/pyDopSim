from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt, QTimer

from game.data_types.api_package import IndicatorState, IndicatorColor


class AbstractIndicator(QWidget):
    def __init__(self, indicator_color: IndicatorColor, text: str, parent=None):
        QWidget.__init__(self, parent=parent)
        self.color: str = indicator_color
        self.setGeometry(0, 0, 70, 60)
        self.state: IndicatorState = IndicatorState.OFF

        self.off_pixmap = QPixmap("assets/indicator_off.png")
        self.on_pixmap = QPixmap(
            f"assets/indicator_on_{indicator_color.name.lower()}.png"
        )

        self.timer = QTimer(self)
        self.timer.timeout.connect(self._update)

        self.body = QLabel("", self)
        self.body.setGeometry(25, 0, 22, 22)
        self.body.setPixmap(self.off_pixmap)
        self.body.setScaledContents(True)

        self.label = QLabel(text, self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setFont(QFont("Arial", 10))
        self.label.setStyleSheet("background-color: white; color: black;")
        self.label.move(0, 23)

    def set_state(self, state: IndicatorState):
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
