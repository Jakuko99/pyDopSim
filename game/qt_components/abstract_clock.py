from PyQt5.QtWidgets import QWidget, QApplication, QLCDNumber
from PyQt5.QtCore import QTimer, QTime
import logging


class AbstractClock(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.logger = logging.getLogger("App.Clock")
        self.logger.setLevel(logging.DEBUG)
        self.logger.debug("AbstractClock initialized")

        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.setStyleSheet("background-color: black; color: red;")
        self.timer.start(500)
        self.display = QLCDNumber(self)
        self.display.setDigitCount(8)
        self.display.display("00:00:00")
        self.display.setSegmentStyle(QLCDNumber.Flat)
        self.display.setFixedSize(200, 50)
        self.display.move(0, 0)

    def update(self):
        time = QTime.currentTime()
        text = time.toString("hh:mm:ss")
        self.display.display(text)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    clock = AbstractClock()
    clock.show()
    sys.exit(app.exec_())
