from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtCore import QTimer

from game.data_types.api_package import SignalSign, SignalType


class AbstractTrackSignal(QWidget):
    def __init__(self, signal_type: SignalType, flipped: bool = False, parent=None):
        QWidget.__init__(self, parent=parent)
        self.signal_type: SignalType = signal_type
        self.flipped: bool = flipped  # rotated 180 degrees
        self.body = QLabel(self)

        if (
            self.signal_type == SignalType.EXPECT_SIGNAL
        ) or self.signal_type == SignalType.SHUNTING_SIGNAL:
            self.setGeometry(0, 0, 35, 28)
            self.off_pixmap = QPixmap("assets/shunt_signal_off.png").transformed(
                QTransform().rotate(180 if self.flipped else 0)
            )
            self.shunt_pixmap = QPixmap("assets/shunt_signal_on.png").transformed(
                QTransform().rotate(180 if self.flipped else 0)
            )
            self.free_pixmap = QPixmap("assets/shunt_signal_free.png").transformed(
                QTransform().rotate(180 if self.flipped else 0)
            )

            self.body.setGeometry(0, 0, 35, 28)
            self.body.setPixmap(self.off_pixmap)

        elif self.signal_type == SignalType.ENTRY_SIGNAL:
            self.setGeometry(0, 0, 120, 29)
            self.stop_pixmap = QPixmap("assets/entry_signal_stop.png").transformed(
                QTransform().rotate(180 if self.flipped else 0)
            )
            self.free_pixmap = QPixmap("assets/entry_signal_free.png").transformed(
                QTransform().rotate(180 if self.flipped else 0)
            )
            self.warn_pixmap = QPixmap("assets/entry_signal_warn.png").transformed(
                QTransform().rotate(180 if self.flipped else 0)
            )
            self.sumonn_pixmap = QPixmap("assets/entry_signal_summon.png").transformed(
                QTransform().rotate(180 if self.flipped else 0)
            )

            self.body.setGeometry(0, 0, 120, 29)
            self.body.setPixmap(self.stop_pixmap)

        elif self.signal_type == SignalType.DEPARTURE_SIGNAL:
            self.setGeometry(0, 0, 62, 29)
            self.off_pixmap = QPixmap("assets/track_signal_off.png").transformed(
                QTransform().rotate(180 if self.flipped else 0)
            )
            self.free_pixmap = QPixmap("assets/track_signal_free.png").transformed(
                QTransform().rotate(180 if self.flipped else 0)
            )
            self.shunt_pixmap = QPixmap("assets/track_signal_shunt.png").transformed(
                QTransform().rotate(180 if self.flipped else 0)
            )

            self.body.setGeometry(0, 0, 60, 27)
            self.body.setScaledContents(True)
            self.body.setPixmap(self.off_pixmap)

        self.state: SignalSign = SignalSign.STOP
        self.timer = QTimer(self)
        self.timer.timeout.connect(self._update)
        self.blinking_lamp: list = None
        self.lamp_state: bool = True

    def set_sign(self, state: SignalSign):
        self.timer.stop()
        if state == SignalSign.SHUNT and (
            self.signal_type == SignalType.SHUNTING_SIGNAL
            or self.signal_type == SignalType.DEPARTURE_SIGNAL
        ):
            self.state = SignalSign.SHUNT
            self.body.setPixmap(self.shunt_pixmap)
        elif state == SignalSign.FREE:
            self.state = SignalSign.FREE
            self.body.setPixmap(self.free_pixmap)
        elif state == SignalSign.STOP:
            self.state = SignalSign.STOP
            if self.signal_type == SignalType.ENTRY_SIGNAL:
                self.body.setPixmap(self.stop_pixmap)
            else:
                self.body.setPixmap(self.off_pixmap)
        elif state == SignalSign.WARN and self.signal_type == SignalType.ENTRY_SIGNAL:
            self.state = SignalSign.WARN
            self.body.setPixmap(self.warn_pixmap)

        elif state == SignalSign.SUMMON and self.signal_type == SignalType.ENTRY_SIGNAL:
            self.state = SignalSign.SUMMON
            self.body.setPixmap(self.sumonn_pixmap)
            self.timer.start(500)

        else:  # failsafe
            if self.signal_type == SignalType.ENTRY_SIGNAL:
                self.body.setPixmap(self.stop_pixmap)
            else:
                self.body.setPixmap(self.off_pixmap)

    def _update(self):
        if self.lamp_state:
            self.body.setPixmap(self.stop_pixmap)
        else:
            self.body.setPixmap(self.sumonn_pixmap)
        self.lamp_state = not self.lamp_state  # invert state
