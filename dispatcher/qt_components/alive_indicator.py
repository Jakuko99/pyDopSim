from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer

from game.data_types.api_package import IndicatorState


class AliveIndicator(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.setGeometry(0, 0, 40, 40)
        self.state: IndicatorState = IndicatorState.OFF

        self.off_pixmap = QPixmap("assets/indicator_vertical.png")
        self.on_pixmap = QPixmap("assets/indicator_horizontal.png")

        self.timer = QTimer(self)
        self.timer.timeout.connect(self._update)
        self.timer.start(1000)

        self.body = QLabel("", self)
        self.body.setGeometry(0, 0, 40, 40)
        self.body.setPixmap(self.off_pixmap)
        self.body.setScaledContents(True)

    def _update(self):
        if self.state == IndicatorState.OFF:
            self.state = IndicatorState.ON
            self.body.setPixmap(self.on_pixmap)
        else:
            self.state = IndicatorState.OFF
            self.body.setPixmap(self.off_pixmap)
