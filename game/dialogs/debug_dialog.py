import os
from PyQt5.QtWidgets import (
    QMainWindow,
    QLabel,
    QPushButton,
    QComboBox,
    QLineEdit,
    QAction,
    QDialog,
)
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtCore import Qt
import logging

from game.qt_components.api_package import (
    AbstractIndicator,
    AbstractSignal,
    AbstractSwitchIndicator,
    AbstractIndicatorSlim,
    AbstractSwitch,
    AbstractTrack,
    AbstractTrackSignal,
    AbstractLeverSlim,
)

from game.data_types.api_package import (
    TrackState,
    SwitchType,
    SignalType,
    SwitchPosition,
    IndicatorColor,
    IndicatorState,
    LeverState,
    SignalSign,
)


class DebugDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.font_obj = QFont("Arial", 11)

        self.logger = logging.getLogger("App.DebugDialog")
        self.logger.setLevel(logging.DEBUG)
        self.logger.debug("Debug Dialog created")
        self.setWindowIcon(QIcon("assets/debug_icon.png"))
        self.font_obj = QFont("Arial", 10)
        self.setFixedSize(505, 500)

        self.setWindowTitle("Debug Window")

        self.object_combo = QComboBox(self)
        self.object_combo.move(5, 5)
        self.station_obj = parent.__dict__

        del self.station_obj["logger"]  # remove extra attributes
        del self.station_obj["log_pipe"]
        del self.station_obj["background"]
        del self.station_obj["font_obj"]
        del self.station_obj["title"]
        del self.station_obj["clock"]

        self.object_combo.addItems(parent.__dict__.keys())
        self.object_combo.setFont(self.font_obj)
        self.object_combo.currentIndexChanged.connect(self.object_selected)

        self.value_combo = QComboBox(self)
        self.value_combo.move(215, 5)
        self.value_combo.setFont(self.font_obj)
        self.value_combo.setFixedWidth(150)
        self.value_combo.setEnabled(False)

        self.set_value_button = QPushButton("Nastaviť hodnotu", self)
        self.set_value_button.move(370, 3)
        self.set_value_button.setFont(self.font_obj)
        self.set_value_button.clicked.connect(self.value_selected)

        self.object_type = QLabel(self)
        self.object_type.move(5, 30)
        self.object_type.setFixedSize(450, 20)

        self.object_state = QLabel(self)
        self.object_state.move(5, 50)
        self.object_state.setFixedSize(200, 20)

    def object_selected(self):
        obj_type = type(self.station_obj[self.object_combo.currentText()])
        self.object_type.setText(str(obj_type))
        self.value_combo.clear()
        self.value_combo.setEnabled(False)

        if obj_type == AbstractSignal or obj_type == AbstractTrackSignal:
            self.value_combo.addItems(SignalSign.__members__.keys())
            self.object_state.setText(
                f"{self.station_obj[self.object_combo.currentText()].state}"
            )
            self.value_combo.setEnabled(True)

        elif obj_type in [AbstractIndicator, AbstractIndicatorSlim]:
            self.value_combo.addItems(IndicatorState.__members__.keys())
            self.value_combo.setEnabled(True)

        elif obj_type in [AbstractTrack, AbstractSwitch]:
            self.value_combo.addItems(TrackState.__members__.keys())
            self.value_combo.setEnabled(True)

        elif obj_type == AbstractLeverSlim:
            self.value_combo.addItems(LeverState.__members__.keys())
            self.value_combo.setEnabled(True)

    def value_selected(self):
        obj_type = type(self.station_obj[self.object_combo.currentText()])

        if obj_type == AbstractSignal or obj_type == AbstractTrackSignal:
            self.station_obj[self.object_combo.currentText()].set_sign(
                SignalSign[self.value_combo.currentText()]
            )
            self.object_state.setText(
                f"{self.station_obj[self.object_combo.currentText()].state}"
            )
        elif obj_type in [
            AbstractIndicator,
            AbstractIndicatorSlim,
            AbstractSwitchIndicator,
        ]:
            self.station_obj[self.object_combo.currentText()].set_state(
                IndicatorState[self.value_combo.currentText()]
            )
        elif obj_type in [AbstractTrack, AbstractSwitch]:
            self.station_obj[self.object_combo.currentText()].set_state(
                TrackState[self.value_combo.currentText()]
            )
        elif obj_type == AbstractLeverSlim:
            self.station_obj[self.object_combo.currentText()]._set_state(
                LeverState[self.value_combo.currentText()]
            )
