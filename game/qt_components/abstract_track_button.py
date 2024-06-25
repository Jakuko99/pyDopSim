from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

from game.data_types.api_package import IndicatorState, IndicatorColor


class AbstractTrackButton(QWidget):
    def __init__(
        self,
        button_color: IndicatorColor,
        parent=None,
        button_name: str = None,
        standalone: bool = False,
    ):
        QWidget.__init__(self, parent=parent)
        self.color: IndicatorColor = button_color
        self.button_name: str = button_name
        self.standalone: bool = standalone
        self.setGeometry(0, 0, 40, 40)
        self.state: IndicatorState = IndicatorState.OFF
        self._state: IndicatorState = IndicatorState.OFF
        self.right_click_function = lambda x: None
        self.middle_click_function = lambda x: None
        self.off_pixmap = QIcon(
            f"assets/track_button_{button_color.name.lower()}_off.png"
        )
        self.on_pixmap = QIcon(
            f"assets/track_button_{button_color.name.lower()}_on.png"
        )
        self._on_clicked = lambda x: None

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
            if not self.standalone:
                self._on_clicked()
            else:
                self._on_clicked(
                    f"T_{self.button_name}_{'S' if self.color == IndicatorColor.WHITE else 'D'}"
                )

        elif self.state == IndicatorState.BLINKING:
            self.set_state(IndicatorState.OFF)

    def set_functions(
        self,
        left_click_function,
        right_click_function,
        middle_click_function=lambda: None,
    ):
        self._on_clicked = left_click_function
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
            if not self.standalone:
                self.right_click_function()
            else:
                self.right_click_function(
                    f"T_{self.button_name}_{'S' if self.color == IndicatorColor.WHITE else 'D'}"
                )
        if QMouseEvent.button() == Qt.MiddleButton:
            if not self.standalone:
                self.middle_click_function()
            else:
                self.middle_click_function(
                    f"T_{self.button_name}_{'S' if self.color == IndicatorColor.WHITE else 'D'}"
                )

    def stop_blinking(self):
        self.timer.stop()
        self.set_state(IndicatorState.OFF)
