from PyQt5.QtWidgets import QWidget, QLabel, QPushButton
from PyQt5 import QtCore
from PyQt5.QtGui import QFont

from game.data_types.api_package import TrackState


class AbstractTrack(QWidget):
    def __init__(self, track_length: int, parent=None):
        QWidget.__init__(self, parent)
        self.setGeometry(0, 0, track_length + 20, 50)
        self.track_length: int = track_length
        font = QFont("Arial", 10, QFont.Bold)

        self.background = QLabel(self)
        self.background.setGeometry(0, 0, track_length, 25)
        self.background.setStyleSheet("background-color: black")

        self.foreground = QLabel(self)
        self.foreground.setGeometry(4, 4, track_length - 8, 17)
        self.foreground.setStyleSheet("background-color: black; color: white;")
        self.foreground.setFont(font)
        self.foreground.setAlignment(QtCore.Qt.AlignCenter)

        self.button_white1 = QPushButton("", self)
        self.button_white1.move(5, 0)
        self.button_white1.resize(25, 25)
        self.button_white1.setStyleSheet(
            "border-radius: 12px; background-color: white; border: 5px solid gray;"
        )

        self.button_green1 = QPushButton("", self)
        self.button_green1.move(32, 0)
        self.button_green1.resize(25, 25)
        self.button_green1.setStyleSheet(
            "border-radius: 12px; background-color: lime; border: 5px solid gray;"
        )

        self.button_white2 = QPushButton("", self)
        self.button_white2.move(track_length - 30, 0)
        self.button_white2.resize(25, 25)
        self.button_white2.setStyleSheet(
            "border-radius: 12px; background-color: white; border: 5px solid gray;"
        )

        self.button_green2 = QPushButton("", self)
        self.button_green2.move(track_length - 57, 0)
        self.button_green2.resize(25, 25)
        self.button_green2.setStyleSheet(
            "border-radius: 12px; background-color: lime; border: 5px solid gray;"
        )

    def set_state(self, state: TrackState, train_id: int = None):
        self.foreground.setText("")

        if state == TrackState.FREE:
            self.foreground.setStyleSheet("background-color: black")
        if state == TrackState.OCCUPIED:
            self.foreground.setStyleSheet("background-color: red; color: white;")
            if train_id:
                self.foreground.setText(
                    f"{train_id} >" if train_id % 2 == 0 else f"< {train_id}"
                )
        if state == TrackState.CLOSURE:
            self.foreground.setStyleSheet("background-color: yellow")
        if state == TrackState.RESERVED:
            self.foreground.setStyleSheet("background-color: gray; color: white;")
            if train_id:
                self.foreground.setText(
                    f"{train_id} >" if train_id % 2 == 0 else f"< {train_id}"
                )
