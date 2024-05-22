from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

from game.data_types.api_package import IndicatorState, IndicatorColor


class AbstractTrackButton(QWidget):
    def __init__(
        self, button_color: IndicatorColor, on_clicked=lambda: None, parent=None
    ):
        QWidget.__init__(self, parent=parent)
        self.color: str = button_color
        self.setGeometry(0, 0, 40, 40)
        self.state: IndicatorState = IndicatorState.OFF
        self._state: IndicatorState = IndicatorState.OFF
        self.right_click_function = lambda: None
        self.middle_click_function = lambda: None
        self.off_pixmap = QIcon(
            f"assets/track_button_{button_color.name.lower()}_off.png"
        )
        self.on_pixmap = QIcon(
            f"assets/track_button_{button_color.name.lower()}_on.png"
        )
        self._on_clicked = on_clicked

        self.timer = QTimer(self)
        self.timer.timeout.connect(self._update)

        self.body = QPushButton("", self)
        self.body.setGeometry(0, 0, 40, 40)
        self.body.setStyleSheet("border-radius: 20px;")
        self.body.setIconSize(self.body.size())
        self.body.setIcon(self.off_pixmap)
        self.body.clicked.connect(self.on_clicked)

    def on_clicked(self):
        if self.state == IndicatorState.OFF:
            self.set_state(IndicatorState.BLINKING)
        elif self.state == IndicatorState.BLINKING:
            self.set_state(IndicatorState.OFF)
        self._on_clicked()  # maybe send event only on activation

    def set_functions(self, right_click_function, middle_click_function=lambda: None):
        self.right_click_function = right_click_function
        self.middle_click_function = middle_click_function

    def set_state(self, state: IndicatorState):
        self.timer.stop()

        if state == IndicatorState.OFF:
            self.state = IndicatorState.OFF
            self.body.setIcon(self.off_pixmap)
        elif state == IndicatorState.BLINKING:
            self.state = IndicatorState.BLINKING
            self.timer.start(500)
            self.body.setIcon(self.on_pixmap)

    def _update(self):
        if self._state == IndicatorState.OFF:
            self._state = IndicatorState.ON
            self.body.setIcon(self.on_pixmap)
        else:
            self._state = IndicatorState.OFF
            self.body.setIcon(self.off_pixmap)

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.RightButton:
            self.right_click_function()
        if QMouseEvent.button() == Qt.MiddleButton:
            self.middle_click_function()
