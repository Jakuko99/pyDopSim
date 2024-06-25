from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5 import QtCore
from PyQt5.QtGui import QFont, QPixmap

from game.data_types.api_package import TrackState, IndicatorColor
from game.qt_components.abstract_track_button import AbstractTrackButton


class AbstractTrack(QWidget):
    def __init__(
        self,
        track_segments: int,
        shunt_track: bool = False,
        no_buttons: bool = False,
        parent=None,
        click_callback=lambda x: None,
        right_click_callback=lambda x: None,
        track_name: str = None,
    ):
        QWidget.__init__(self, parent)
        if no_buttons:
            self.setGeometry(0, 0, (track_segments * 60), 20)
        else:
            self.setGeometry(0, 0, (track_segments * 60) + 180, 46)
        self.track_segments: int = track_segments
        self.track_name: str = track_name
        font = QFont("Arial", 11)
        self.segments: QLabel = []
        self.click_callback = click_callback
        self.right_click_callback = right_click_callback
        self.no_buttons: bool = no_buttons
        self.shunt_track: bool = shunt_track
        self.train_label = None
        self.state: TrackState = TrackState.FREE
        self.test_state: bool = False

        for i in range(track_segments):
            seg = QLabel(self)
            seg.setPixmap(QPixmap("assets/track_free.png"))
            if self.no_buttons:
                seg.move(i * 60, 0)
            else:
                seg.move(90 + i * 60, 17)
            seg.resize(60, 20)
            self.segments.append(seg)

        if self.no_buttons is False:
            self.train_label = QLabel(self)
            self.train_label.setFont(font)
            self.train_label.move(int((120 + (track_segments * 60) + 20) / 2), 0)
            self.train_label.setFixedSize(100, 15)

            self.button_white1 = AbstractTrackButton(IndicatorColor.WHITE, parent=self)
            self.button_white1.set_functions(
                left_click_function=lambda: self.click_callback(
                    f"T_{self.track_name}_S1"
                ),
                right_click_function=lambda: self.right_click_callback(
                    f"T_{self.track_name}_S1"
                ),
            )
            self.button_white1.move(10, 8)

            if not self.shunt_track:
                self.button_green1 = AbstractTrackButton(
                    IndicatorColor.GREEN, parent=self
                )
                self.button_green1.set_functions(
                    left_click_function=lambda: self.click_callback(
                        f"T_{self.track_name}_D1"
                    ),
                    right_click_function=lambda: self.right_click_callback(
                        f"T_{self.track_name}_D1"
                    ),
                )
                self.button_green1.move(50, 8)

                self.button_green2 = AbstractTrackButton(
                    IndicatorColor.GREEN, parent=self
                )
                self.button_green2.set_functions(
                    left_click_function=lambda: self.click_callback(
                        f"T_{self.track_name}_D2"
                    ),
                    right_click_function=lambda: self.right_click_callback(
                        f"T_{self.track_name}_D2"
                    ),
                )
                self.button_green2.move(120 + (track_segments * 60) - 30, 8)

            self.button_white2 = AbstractTrackButton(IndicatorColor.WHITE, parent=self)
            self.button_white2.set_functions(
                left_click_function=lambda: self.click_callback(
                    f"T_{self.track_name}_S2"
                ),
                right_click_function=lambda: self.right_click_callback(
                    f"T_{self.track_name}_S2"
                ),
            )
            self.button_white2.move(160 + (track_segments * 60) - 30, 8)

    def set_state(self, state: TrackState, train_id: int = None):
        self.state = state
        if self.train_label:
            self.train_label.setText("")

        segment: QLabel
        if state == TrackState.FREE:
            for segment in self.segments:
                segment.setPixmap(QPixmap("assets/track_free.png"))
        if state == TrackState.OCCUPIED:
            for segment in self.segments:
                segment.setPixmap(QPixmap("assets/track_occupied.png"))
            if train_id:
                self.train_label.setText(
                    f"{train_id} >" if train_id % 2 == 0 else f"< {train_id}"
                )
        if state == TrackState.CLOSURE:
            pass  # TODO: add closure state
        if state == TrackState.RESERVED:
            for segment in self.segments:
                segment.setPixmap(QPixmap("assets/track_reserved.png"))
            if train_id:
                self.train_label.setText(
                    f"{train_id} >" if train_id % 2 == 0 else f"< {train_id}"
                )

    def set_segment(self, segment_id: int, state: TrackState):
        if segment_id < len(self.segments):
            segment = self.segments[segment_id]
            if state == TrackState.FREE:
                segment.setPixmap(QPixmap("assets/track_free.png"))
            if state == TrackState.OCCUPIED:
                segment.setPixmap(QPixmap("assets/track_occupied.png"))
            if state == TrackState.RESERVED:
                segment.setPixmap(QPixmap("assets/track_reserved.png"))
            if state == TrackState.CLOSURE:
                pass

    def check_state(self, action: bool = False):
        if self.state == TrackState.FREE and action is True:
            self.set_state(TrackState.RESERVED)
            self.test_state = True
        elif (
            action is False
            and not (self.state is TrackState.RESERVED or TrackState.OCCUPIED)
            or self.test_state is True
        ):
            self.set_state(TrackState.FREE)
            self.test_state = False

    def stop_blinking(self):
        self.button_white1.stop_blinking()
        self.button_white2.stop_blinking()

        if not self.shunt_track:
            self.button_green1.stop_blinking()
            self.button_green2.stop_blinking()
