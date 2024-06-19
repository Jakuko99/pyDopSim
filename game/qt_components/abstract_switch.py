from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap, QTransform

from game.data_types.api_package import TrackState, SwitchType, SwitchPosition
from game.qt_components.abstract_track import AbstractTrack


class AbstractSwitch(QWidget):
    def __init__(self, switch_type: SwitchType, parent=None):
        QWidget.__init__(self, parent)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self._update)
        self.state: bool = False
        self.test_state: bool = False
        self.switch_type: SwitchType = switch_type

        if switch_type == SwitchType.Z_TYPE:
            switch_height: int = 100
        else:
            switch_height: int = 60

        self.setGeometry(0, 0, 60, switch_height)
        self.switch_type: SwitchType = switch_type
        self.occupancy_status: TrackState = TrackState.FREE
        self.test_state: bool = False
        self.switch_position: SwitchPosition = (
            SwitchPosition.STRAIGHT
            if not switch_type == SwitchType.Z_TYPE
            else SwitchPosition.TURNED
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

            self.diagonal = QLabel(self)
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

    def set_state(self, state: TrackState, position: SwitchPosition = None):
        """position - for Z switch to specify which track is occupied"""

        if not state is TrackState.ALL or TrackState.TEST:
            self.occupancy_status = state  # dont save state if flashing

        self.diagonal.setPixmap(self.free_diagonal_pixmap)  # reset pixmaps
        if self.switch_type == SwitchType.Z_TYPE:
            self.straight_up.setPixmap(self.free_straight_pixmap)
            self.straight_down.setPixmap(self.free_straight_pixmap)

        if self.associated_track.get("down", None):
            self.associated_track["down"].set_state(TrackState.FREE)
        if self.associated_track.get("up", None):
            self.associated_track["up"].set_state(TrackState.FREE)

        if self.switch_type == SwitchType.Z_TYPE:
            if self.switch_position is SwitchPosition.TURNED:
                self.diagonal.setPixmap(
                    self.occupied_diagonal_pixmap
                    if state == TrackState.OCCUPIED
                    else (
                        self.reserved_diagonal_pixmap
                        if state == TrackState.RESERVED
                        else self.free_diagonal_pixmap
                    )
                )
            elif self.switch_position is SwitchPosition.Z_DOWN_STRAIGHT:
                self.straight_down.setPixmap(
                    self.occupied_straight_pixmap
                    if state == TrackState.OCCUPIED
                    else (
                        self.reserved_straight_pixmap
                        if state == TrackState.RESERVED
                        else self.free_straight_pixmap
                    )
                )
            elif self.switch_position is SwitchPosition.Z_UP_STRAIGHT:
                self.straight_up.setPixmap(
                    self.occupied_straight_pixmap
                    if state == TrackState.OCCUPIED
                    else (
                        self.reserved_straight_pixmap
                        if state == TrackState.RESERVED
                        else self.free_straight_pixmap
                    )
                )
            elif self.switch_position is SwitchPosition.Z_BOTH:
                if position:  # set only specified segment of the switch
                    if position == SwitchPosition.Z_DOWN_STRAIGHT:
                        self.straight_down.setPixmap(
                            self.occupied_straight_pixmap
                            if state == TrackState.OCCUPIED
                            else (
                                self.reserved_straight_pixmap
                                if state == TrackState.RESERVED
                                else self.free_straight_pixmap
                            )
                        )
                    elif position == SwitchPosition.Z_UP_STRAIGHT:
                        self.straight_up.setPixmap(
                            self.occupied_straight_pixmap
                            if state == TrackState.OCCUPIED
                            else (
                                self.reserved_straight_pixmap
                                if state == TrackState.RESERVED
                                else self.free_straight_pixmap
                            )
                        )
                else:  # set all segments of the switch
                    self.straight_up.setPixmap(
                        self.occupied_straight_pixmap
                        if state == TrackState.OCCUPIED
                        else (
                            self.reserved_straight_pixmap
                            if state == TrackState.RESERVED
                            else self.free_straight_pixmap
                        )
                    )
                    self.straight_down.setPixmap(
                        self.occupied_straight_pixmap
                        if state == TrackState.OCCUPIED
                        else (
                            self.reserved_straight_pixmap
                            if state == TrackState.RESERVED
                            else self.free_straight_pixmap
                        )
                    )

            if state == TrackState.ALL:
                self.diagonal.setPixmap(self.occupied_diagonal_pixmap)
                self.straight_up.setPixmap(self.occupied_straight_pixmap)
                self.straight_down.setPixmap(self.occupied_straight_pixmap)
            elif state == TrackState.TEST:
                self.diagonal.setPixmap(self.reserved_diagonal_pixmap)
                self.straight_up.setPixmap(self.reserved_straight_pixmap)
                self.straight_down.setPixmap(self.reserved_straight_pixmap)

        else:
            if self.switch_position == SwitchPosition.TURNED:
                self.diagonal.setPixmap(
                    self.occupied_diagonal_pixmap
                    if state == TrackState.OCCUPIED
                    else (
                        self.reserved_diagonal_pixmap
                        if state == TrackState.RESERVED
                        else self.free_diagonal_pixmap
                    )
                )
                if self.switch_type == SwitchType.UP_45_LEFT:
                    if self.associated_track.get("up", None):
                        self.associated_track["up"].set_state(state)
                elif self.switch_type == SwitchType.UP_45_RIGHT:
                    if self.associated_track.get("down", None):
                        self.associated_track["down"].set_segment(0, state)

            elif self.switch_position == SwitchPosition.STRAIGHT:
                if (
                    self.switch_type == SwitchType.DOWN_45_LEFT
                    or SwitchType.DOWN_45_RIGHT
                ):
                    if self.associated_track.get("down", None):
                        self.associated_track["down"].set_state(state)

                elif (
                    self.switch_type == SwitchType.UP_45_LEFT or SwitchType.UP_45_RIGHT
                ):
                    if self.associated_track.get("up", None):
                        self.associated_track["up"].set_state(state)

            if state == TrackState.ALL:
                self.diagonal.setPixmap(self.occupied_diagonal_pixmap)
                if self.associated_track.get("down", None):
                    self.associated_track["down"].set_state(TrackState.OCCUPIED)
                if self.associated_track.get("up", None):
                    self.associated_track["up"].set_state(TrackState.OCCUPIED)
            elif state == TrackState.TEST:
                self.diagonal.setPixmap(self.reserved_diagonal_pixmap)
                if self.associated_track.get("down", None):
                    self.associated_track["down"].set_state(TrackState.RESERVED)
                if self.associated_track.get("up", None):
                    self.associated_track["up"].set_state(TrackState.RESERVED)

    def set_position(self, position: SwitchPosition):
        if self.switch_type == SwitchType.Z_TYPE:
            if position in [
                SwitchPosition.TURNED,
                SwitchPosition.Z_DOWN_STRAIGHT,
                SwitchPosition.Z_UP_STRAIGHT,
                SwitchPosition.Z_BOTH,
            ]:
                self.switch_position = position
        elif position in [SwitchPosition.STRAIGHT, SwitchPosition.TURNED]:
            self.switch_position = position
        elif position == SwitchPosition.AUTO:
            pass  # no action needed
        else:
            raise ValueError(f"Invalid switch position for switch {self.switch_type}")

        self.set_state(self.occupancy_status, position)  # update state of the switch

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

    def toggle_blinking_action(self):
        if self.timer.isActive():
            self.timer.stop()
        else:
            self.timer.start(500)

    def start_blinking_action(self):
        if not self.timer.isActive():
            self.timer.start(500)

    def stop_blinking_action(self):
        if self.timer.isActive():
            self.timer.stop()

    def check_state(self, action: bool = False):
        if self.occupancy_status == TrackState.FREE and action is True:
            self.set_state(TrackState.RESERVED)
            self.test_state = True
        elif (
            action is False
            and not (
                self.occupancy_status is TrackState.RESERVED or TrackState.OCCUPIED
            )
            or self.test_state is True
        ):
            self.set_state(TrackState.FREE)
            self.test_state = False

    def check_occupancy(self, action: bool = False):
        if self.occupancy_status == TrackState.FREE and action is True:
            self.set_state(TrackState.TEST)
            self.test_state = True
        elif action is False and self.test_state is True:
            self.set_state(TrackState.FREE)
            self.test_state = False

    def _update(self):
        if self.state:
            self.set_state(TrackState.ALL)
        else:
            self.set_state(TrackState.FREE)

        self.state = not self.state
