from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QTransform

from game.data_types.api_package import TrackState, SwitchType


class AbstractSwitch(QWidget):
    def __init__(self, switch_type: SwitchType, parent=None):
        QWidget.__init__(self, parent)
        self.switch_type: SwitchType = switch_type
        if switch_type == SwitchType.Z_TYPE:
            switch_height: int = 90
        else:
            switch_height: int = 45
        self.setGeometry(0, 0, 60, switch_height)
        self.switch_type: SwitchType = switch_type
        self.occupancy_status: TrackState = TrackState.FREE

        if self.switch_type == SwitchType.Z_TYPE:
            self.free_straight_pixmap: QPixmap = QPixmap("assets/track_free.png")
            self.reserved_straight_pixmap: QPixmap = QPixmap(
                "assets/track_reserved.png"
            )
            self.occupied_straight_pixmap: QPixmap = QPixmap(
                "assets/track_occupied.png"
            )
            self.free_diagonal_pixmap: QPixmap = QPixmap(
                "assets/diagonal_track_free.png"
            )
            self.reserved_diagonal_pixmap: QPixmap = QPixmap(
                "assets/diagonal_track_reserved.png"
            )
            self.occupied_diagonal_pixmap: QPixmap = QPixmap(
                "assets/diagonal_track_occupied.png"
            )

            self.straight_up = QLabel(self)
            self.straight_up.setGeometry(0, 0, 60, 21)
            self.straight_up.setPixmap(self.free_straight_pixmap)
            self.straight_up.move(0, 0)

            self.straight_down = QLabel(self)
            self.straight_down.setGeometry(0, 0, 60, 21)
            self.straight_down.setPixmap(self.free_straight_pixmap)
            self.straight_down.move(0, 65)

            self.diagonal = QLabel(self)
            self.diagonal.setGeometry(0, 0, 45, 45)
            self.diagonal.setPixmap(self.free_diagonal_pixmap)
            self.diagonal.setScaledContents(True)
            self.diagonal.setStyleSheet("background-color: transparent")
            self.diagonal.move(5, 21)

        else:
            self.free_diagonal_pixmap: QPixmap = QPixmap(
                "assets/diagonal_track_free.png"
            )
            self.reserved_diagonal_pixmap: QPixmap = QPixmap(
                "assets/diagonal_track_reserved.png"
            )
            self.occupied_diagonal_pixmap: QPixmap = QPixmap(
                "assets/diagonal_track_occupied.png"
            )

            if self.switch_type == SwitchType.UP_45_LEFT:
                self.free_diagonal_pixmap = QPixmap(
                    "assets/diagonal_track_flipped_free.png"
                ).transformed(QTransform().rotate(180))
                self.reserved_diagonal_pixmap = QPixmap(
                    "assets/diagonal_track_flipped_reserved.png"
                ).transformed(QTransform().rotate(180))
                self.occupied_diagonal_pixmap = QPixmap(
                    "assets/diagonal_track_flipped_occupied.png"
                ).transformed(QTransform().rotate(180))
            elif self.switch_type == SwitchType.UP_45_RIGHT:
                pass  # image is already rotated
            elif self.switch_type == SwitchType.DOWN_45_LEFT:
                self.free_diagonal_pixmap = self.free_diagonal_pixmap.transformed(
                    QTransform().rotate(180)
                )
                self.reserved_diagonal_pixmap = (
                    self.reserved_diagonal_pixmap.transformed(QTransform().rotate(180))
                )
                self.occupied_diagonal_pixmap = (
                    self.occupied_diagonal_pixmap.transformed(QTransform().rotate(180))
                )
            elif self.switch_type == SwitchType.DOWN_45_RIGHT:
                self.free_diagonal_pixmap = QPixmap(
                    "assets/diagonal_track_flipped_free.png"
                )
                self.reserved_diagonal_pixmap = QPixmap(
                    "assets/diagonal_track_flipped_reserved.png"
                )
                self.occupied_diagonal_pixmap = QPixmap(
                    "assets/diagonal_track_flipped_occupied.png"
                )
            else:
                raise ValueError("Invalid switch type")

            self.diagonal = QLabel(self)
            self.diagonal.setGeometry(0, 0, 45, 45)
            self.diagonal.setPixmap(self.free_diagonal_pixmap)
            self.diagonal.setScaledContents(True)
            self.diagonal.setStyleSheet("background-color: transparent")
            self.diagonal.move(0, 0)

    def set_state(self, state: TrackState):
        if self.switch_type == SwitchType.Z_TYPE:
            if state == TrackState.FREE:
                self.straight_up.setPixmap(self.free_straight_pixmap)
                self.straight_down.setPixmap(self.free_straight_pixmap)
                self.diagonal.setPixmap(self.free_diagonal_pixmap)
            elif state == TrackState.RESERVED:
                self.straight_up.setPixmap(self.reserved_straight_pixmap)
                self.straight_down.setPixmap(self.reserved_straight_pixmap)
                self.diagonal.setPixmap(self.reserved_diagonal_pixmap)
            elif state == TrackState.OCCUPIED:
                self.straight_up.setPixmap(self.occupied_straight_pixmap)
                self.straight_down.setPixmap(self.occupied_straight_pixmap)
                self.diagonal.setPixmap(self.occupied_diagonal_pixmap)

        else:
            if state == TrackState.FREE:
                self.diagonal.setPixmap(self.free_diagonal_pixmap)
            elif state == TrackState.RESERVED:
                self.diagonal.setPixmap(self.reserved_diagonal_pixmap)
            elif state == TrackState.OCCUPIED:
                self.diagonal.setPixmap(self.occupied_diagonal_pixmap)
