from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5 import QtCore
from PyQt5.QtGui import QFont, QPainter

from game.data_types.api_package import TrackState, SwitchType

# needs rework, especially the angled part


class MyLabel(QWidget):
    def __init__(self, text: str, angle: int, parent=None):
        QWidget.__init__(self, parent)
        self.text = text
        self.angle = angle

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QtCore.Qt.black)
        painter.translate(20, 100)
        painter.rotate(self.angle)
        painter.drawText(0, 0, self.text)
        painter.end()


class AbstractSwitch(QWidget):
    def __init__(self, switch_length: int, switch_type: SwitchType, parent=None):
        QWidget.__init__(self, parent)
        self.setGeometry(0, 0, switch_length, switch_length)
        self.switch_length: int = switch_length
        self.switch_type: SwitchType = switch_type

        self.label = MyLabel("text", 45, parent)  # not working
        self.label.setStyleSheet("background-color: black;")
        self.label.move(0, 0)

    def set_state(self, state: TrackState):
        if state == TrackState.FREE:
            self.foreground.setStyleSheet("background-color: black;")
        if state == TrackState.OCCUPIED:
            self.foreground.setStyleSheet("background-color: red;")
        if state == TrackState.CLOSURE:
            self.foreground.setStyleSheet("background-color: yellow;")
        if state == TrackState.RESERVED:
            self.foreground.setStyleSheet("background-color: gray;")
