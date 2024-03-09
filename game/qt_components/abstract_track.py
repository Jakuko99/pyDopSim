from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5 import QtCore
from PyQt5.QtGui import QFont

from game.data_types.api_package import TrackState


class AbstractTrack(QWidget):
    def __init__(self, track_lenght: int, parent=None):
        QWidget.__init__(self, parent)
        self.setGeometry(0, 0, track_lenght + 20, 30)
        self.track_lenght: int = track_lenght
        font = QFont("Arial", 10, QFont.Bold)

        self.background = QLabel(self)
        self.background.setGeometry(0, 0, track_lenght, 25)
        self.background.setStyleSheet("background-color: black")

        self.foreground = QLabel(self)
        self.foreground.setGeometry(4, 4, track_lenght - 8, 17)
        self.foreground.setStyleSheet("background-color: black; color: white;")        
        self.foreground.setFont(font)
        self.foreground.setAlignment(QtCore.Qt.AlignCenter)

    def set_state(self, state: TrackState, train_id: int = None):
        self.foreground.setText("")

        if state == TrackState.FREE:
            self.foreground.setStyleSheet("background-color: black")
        if state == TrackState.OCCUPIED:
            self.foreground.setStyleSheet("background-color: red; color: white;")
            if train_id:
                self.foreground.setText(f"{train_id}>" if train_id % 2 == 0 else f"<{train_id}")
        if state == TrackState.CLOSURE:
            self.foreground.setStyleSheet("background-color: yellow")
        if state == TrackState.RESERVED:
            self.foreground.setStyleSheet("background-color: gray; color: white;")
            if train_id:
                self.foreground.setText(f"{train_id}>" if train_id % 2 == 0 else f"<{train_id}")
