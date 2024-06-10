from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap, QTransform

from game.data_types.api_package import TrackState, SwitchType, SwitchPosition
from game.qt_components.abstract_track import AbstractTrack


class AbstractSwitch(QWidget):
    def __init__(self, switch_type: SwitchType, parent=None):
        QWidget.__init__(self, parent)
        self.timer = QTimer(self)
        self.switch_type: SwitchType = switch_type
        if switch_type == SwitchType.Z_TYPE:
            switch_height: int = 100
        else:
            switch_height: int = 60
        self.setGeometry(0, 0, 60, switch_height)
        self.switch_type: SwitchType = switch_type
        self.occupancy_status: TrackState = TrackState.FREE
        self.switch_position: SwitchPosition = (
            SwitchPosition.STRAIGHT
            if not switch_type == SwitchType.Z_TYPE
            else SwitchPosition.Z_DOWN_STRAIGHT
        )
        self.associated_track: dict[AbstractTrack] = dict()

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
            self.straight_down.move(0, 78)

            self.diagonal = QLabel(
                self
            )  # TODO: diagonal visual asset needs to be redone, doesn't line correctly
            self.diagonal.setGeometry(0, 0, 60, 60)
            self.diagonal.setPixmap(self.free_diagonal_pixmap)
            self.diagonal.setScaledContents(True)
            self.diagonal.setStyleSheet("background-color: transparent")
            self.diagonal.move(6, 19)

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
            self.diagonal.setGeometry(0, 0, 60, 60)
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

        if (
            self.associated_track
        ):  # copy state to associated track object, switch can have up to two objects
            if self.associated_track.get("down", None):
                self.associated_track.get("down").set_state(state)

            if self.associated_track.get("up", None):
                self.associated_track.get("up").set_state(state)

    def add_associated_track(
        self,
        default_track: AbstractTrack,
        additional_track: AbstractTrack = None,
    ):
        """default_track - main track associated with the switch (down)
        additional_track - additional track associated with the switch, placed on the other side of the switch (up)
        """
        if additional_track:
            self.associated_track["up"] = additional_track

        self.associated_track["down"] = default_track

    def blinking_action(self):
        pass  # TODO: implement blinking action when creating path for train
