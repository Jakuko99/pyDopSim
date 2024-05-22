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
        parent=None,
        click_callaback=lambda x: None,
        right_click_callback=lambda x: None,
    ):
        QWidget.__init__(self, parent)
        self.setGeometry(0, 0, (track_segments * 60) + 180, 46)
        self.track_segments: int = track_segments
        font = QFont("Arial", 11)
        self.segments: QLabel = []
        self.click_callaback = click_callaback
        self.right_click_callback = right_click_callback

        self.train_label = QLabel(self)
        self.train_label.setFont(font)
        self.train_label.move(int((120 + (track_segments * 60) + 20) / 2), 0)
        self.train_label.setFixedSize(100, 15)

        for i in range(track_segments):
            seg = QLabel(self)
            seg.setPixmap(QPixmap("assets/track_free.png"))
            seg.move(90 + i * 60, 17)
            seg.resize(60, 20)
            self.segments.append(seg)

        self.button_white1 = AbstractTrackButton(
            IndicatorColor.WHITE,
            parent=self,
            on_clicked=lambda: self.click_callaback(1),
        )
        self.button_white1.set_functions(
            right_click_function=lambda: self.right_click_callback(1)
        )
        self.button_white1.move(10, 8)

        if not shunt_track:
            self.button_green1 = AbstractTrackButton(
                IndicatorColor.GREEN,
                parent=self,
                on_clicked=lambda: self.click_callaback(2),
            )
            self.button_green1.set_functions(
                right_click_function=lambda: self.right_click_callback(2)
            )
            self.button_green1.move(50, 8)

            self.button_green2 = AbstractTrackButton(
                IndicatorColor.GREEN,
                parent=self,
                on_clicked=lambda: self.click_callaback(3),
            )
            self.button_green2.set_functions(
                right_click_function=lambda: self.right_click_callback(3)
            )
            self.button_green2.move(120 + (track_segments * 60) - 30, 8)

        self.button_white2 = AbstractTrackButton(
            IndicatorColor.WHITE,
            parent=self,
            on_clicked=lambda: self.click_callaback(4),
        )
        self.button_white2.set_functions(
            right_click_function=lambda: self.right_click_callback(4)
        )
        self.button_white2.move(160 + (track_segments * 60) - 30, 8)

    def set_state(self, state: TrackState, train_id: int = None):
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
