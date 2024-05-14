from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QComboBox, QLineEdit
from PyQt5.QtGui import QIcon

from game.qt_components.api_package import (
    AbstractSignal,
    AbstractTrack,
    AbstractSwitch,
    AbstractIndicator,
    AbstractIndicatorSlim,
    AbstractLever,
    AbstractButton,
    AbstractStationButton,
)
from game.forms.station_platforms import StationPlatforms
from game.data_types.api_package import (
    SignalSign,
    TrackState,
    SwitchType,
    IndicatorState,
    IndicatorColor,
    LeverState,
    ButtonType,
)


class TestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 800, 600)
        self.setWindowTitle("Component test window")
        self.setStyleSheet("background-color: lightgray")

        self.platforms: StationPlatforms = StationPlatforms()

        self.signal = AbstractSignal(5, self)
        self.signal.move(40, 5)

        self.combo = QComboBox(self)
        self.combo.addItems([item for item in SignalSign.__members__])
        self.combo.move(5, 90)
        self.button = QPushButton("Change signal", self)
        self.button.move(5, 125)
        self.button.clicked.connect(self.change_signal)

        self.signal1 = AbstractSignal(2, self)
        self.signal1.move(160, 5)

        self.combo1 = QComboBox(self)
        self.combo1.addItems([item for item in SignalSign.__members__])
        self.combo1.move(120, 90)
        self.button1 = QPushButton("Change signal", self)
        self.button1.move(120, 125)
        self.button1.clicked.connect(self.change_signal1)

        self.signal2 = AbstractSignal(3, self)
        self.signal2.move(280, 5)

        self.combo2 = QComboBox(self)
        self.combo2.addItems([item for item in SignalSign.__members__])
        self.combo2.move(240, 90)
        self.button2 = QPushButton("Change signal", self)
        self.button2.move(240, 125)
        self.button2.clicked.connect(self.change_signal2)

        self.station_button = AbstractStationButton(self)
        self.station_button.move(360, 20)
        self.station_button.setFunctions(self.show_platforms)

        self.track = AbstractTrack(300, self)
        self.track.move(5, 180)

        self.combo3 = QComboBox(self)
        self.combo3.addItems([item for item in TrackState.__members__])
        self.combo3.move(5, 210)
        self.label = QLabel("Train ID:", self)
        self.label.move(110, 210)
        self.train_id = QLineEdit("1234", self)
        self.train_id.move(165, 210)
        self.button3 = QPushButton("Change state", self)
        self.button3.move(50, 245)
        self.button3.clicked.connect(self.change_state)

        self.indicator = AbstractIndicator(IndicatorColor.WHITE, "Voľnosť\ntrate", self)
        self.indicator.move(75, 280)

        self.indicator1 = AbstractIndicatorSlim(IndicatorColor.RED, self)
        self.indicator1.move(150, 275)

        self.indicator2 = AbstractIndicatorSlim(IndicatorColor.GREEN, self)
        self.indicator2.move(190, 275)

        self.indicator3 = AbstractIndicatorSlim(IndicatorColor.WHITE, self)
        self.indicator3.move(230, 275)

        self.combo4 = QComboBox(self)
        self.combo4.addItems([item for item in IndicatorState.__members__])
        self.combo4.move(5, 345)
        self.button4 = QPushButton("Change signal", self)
        self.button4.move(110, 345)
        self.button4.clicked.connect(self.change_state1)

        self.lever = AbstractLever("+ 1/3 -", self.change_lever, self)
        self.lever.move(5, 400)

        self.abstract_button = AbstractButton(ButtonType.NORMAL, self)
        self.abstract_button.move(75, 400)

        self.abs_label = QLabel("Button", self)
        self.abs_label.move(75, 440)
        self.abstract_button.setFunctions(
            left_click_function=lambda: self.abs_label.setText("Left click"),
            right_click_function=lambda: self.abs_label.setText("Right click"),
            middle_click_function=lambda: self.abs_label.setText("Middle click"),
        )

    def change_signal(self):
        self.signal.set_sign(SignalSign[self.combo.currentText()])

    def change_signal1(self):
        self.signal1.set_sign(SignalSign[self.combo1.currentText()])

    def change_signal2(self):
        self.signal2.set_sign(SignalSign[self.combo2.currentText()])

    def change_state(self):
        self.track.set_state(
            TrackState[self.combo3.currentText()], int(self.train_id.text())
        )

    def change_state1(self):
        self.indicator.set_state(IndicatorState[self.combo4.currentText()])
        self.indicator1.set_state(IndicatorState[self.combo4.currentText()])
        self.indicator2.set_state(IndicatorState[self.combo4.currentText()])
        self.indicator3.set_state(IndicatorState[self.combo4.currentText()])

    def change_lever(self, state: LeverState):
        self.lever.set_light(1, IndicatorState.OFF)  # reset lights
        self.lever.set_light(2, IndicatorState.OFF)
        self.lever.set_light(3, IndicatorState.OFF)

        if state == LeverState.LEFT:
            self.lever.set_light(1, IndicatorState.ON)
        elif state == LeverState.MIDDLE:
            self.lever.set_light(2, IndicatorState.ON)
        elif state == LeverState.RIGHT:
            self.lever.set_light(3, IndicatorState.ON)

    def show_platforms(self):
        if self.platforms:
            self.platforms.show()
