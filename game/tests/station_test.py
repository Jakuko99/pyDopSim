from queue import Queue
import logging
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import QEventLoop

from game.forms.api_package import REStation
from game.data_types.api_package import (
    IndicatorState,
    TrackState,
    LeverState,
    SwitchPosition,
)
from utils.api_package import queue_handler


class StationTest:
    def __init__(self, log_pipe: Queue = None, station_name: str = "Test station"):
        self.logger = logging.getLogger("App.StationTest")
        self.logger.setLevel(logging.DEBUG)
        self.logger.info("Station test started")
        self.app = QApplication([])
        if log_pipe:
            self.log_pipe = log_pipe
        else:
            self.log_pipe = (
                queue_handler.get_logging_pipe()
            )  # grab the logging pipe from the queue handler
        self.window = REStation(station_name=station_name)
        self.window.setWindowTitle(
            "Station test window"
        )  # override default window title for testing
        self.window.station_button.enable_debug()

    def add_test_bindings(self):
        self.window.path_build_cancel.setFunctions(
            lambda: self.window.path_build.set_state(IndicatorState.ON),  # left click
            lambda: self.window.path_build.set_state(IndicatorState.OFF),  # right click
            lambda: self.window.path_build.set_state(
                IndicatorState.BLINKING
            ),  # middle click
        )
        self.window.switch_1_3_controller.set_update_function(self.switch_1_3_action)
        self.window.switch_2_controller.set_update_function(self.switch_2_action)
        self.window.switch_4_vk2_controller.set_update_function(self.switch_4_action)
        self.window.switch_5_controller.set_update_function(self.switch_5_action)
        self.window.switch_6_7_controller.set_update_function(self.switch_6_7_action)
        self.window.switch_8_controller.set_update_function(self.switch_8_action)
        self.window.switch_9_controller.set_update_function(self.switch_9_action)
        self.window.switch_10_controller.set_update_function(self.switch_10_action)

        self.window.track_1.click_callaback = self.track1_callback
        self.window.track_2.click_callaback = self.track2_callback
        self.window.track_3.click_callaback = self.track3_callback
        self.window.track_5.click_callaback = self.track5_callback
        self.window.track_4.click_callaback = self.track4_callback
        self.window.track_4.right_click_callback = (
            lambda x: self.window.track_4.set_state(TrackState.FREE)
        )

        self.window.check_switch_positions.set_onPress(self.check_switch_positions)
        self.window.check_switch_positions.set_onRelease(self.revert_switch_positions)

        self.window.check_track_segments.set_onPress(self.check_track_occupancy)
        self.window.check_track_segments.set_onRelease(self.revert_track_occupancy)

    def track1_callback(self, button_id: int):
        if button_id == 2:
            self.window.track_1.set_state(TrackState.OCCUPIED, train_id=940)
        elif button_id == 3:
            self.window.track_1.set_state(TrackState.RESERVED, train_id=941)
        elif button_id == 4:
            self.window.track_1.set_state(TrackState.FREE)

    def track2_callback(self, button_id: int):
        if button_id == 2:
            self.window.track_2.set_state(TrackState.OCCUPIED, train_id=940)
        elif button_id == 3:
            self.window.track_2.set_state(TrackState.RESERVED, train_id=941)
        elif button_id == 4:
            self.window.track_2.set_state(TrackState.FREE)

    def track3_callback(self, button_id: int):
        if button_id == 2:
            self.window.track_3.set_state(TrackState.OCCUPIED, train_id=940)
        elif button_id == 3:
            self.window.track_3.set_state(TrackState.RESERVED, train_id=941)
        elif button_id == 4:
            self.window.track_3.set_state(TrackState.FREE)

    def track5_callback(self, button_id: int):
        if button_id == 2:
            self.window.track_5.set_state(TrackState.OCCUPIED, train_id=940)
        elif button_id == 3:
            self.window.track_5.set_state(TrackState.RESERVED, train_id=941)
        elif button_id == 4:
            self.window.track_5.set_state(TrackState.FREE)

    def track4_callback(self, button_id: int):
        if button_id == 1:
            self.window.track_4.set_state(TrackState.OCCUPIED)
        elif button_id == 4:
            self.window.track_4.set_state(TrackState.RESERVED)

    def switch_1_3_action(self, state: LeverState):
        self.window.switch_1_3_controller.set_light(state.value, IndicatorState.ON)
        self.window.switch_1_3.set_position(
            SwitchPosition.Z_DOWN_STRAIGHT
            if state == LeverState.LEFT
            else SwitchPosition.TURNED
            if state == LeverState.MIDDLE
            else SwitchPosition.Z_UP_STRAIGHT
        )

    def switch_5_action(self, state: LeverState):
        self.window.switch_5_controller.set_light(state.value, IndicatorState.ON)
        self.window.switch_5.set_position(
            SwitchPosition.STRAIGHT
            if state == LeverState.LEFT
            else SwitchPosition.AUTO
            if state == LeverState.MIDDLE
            else SwitchPosition.TURNED
        )

    def switch_2_action(self, state: LeverState):
        self.window.switch_2_controller.set_light(state.value, IndicatorState.ON)
        self.window.switch_2.set_position(
            SwitchPosition.STRAIGHT
            if state == LeverState.LEFT
            else SwitchPosition.AUTO
            if state == LeverState.MIDDLE
            else SwitchPosition.TURNED
        )

    def switch_4_action(self, state: LeverState):
        self.window.switch_4_vk2_controller.set_light(state.value, IndicatorState.ON)
        self.window.switch_4.set_position(
            SwitchPosition.STRAIGHT
            if state == LeverState.LEFT
            else SwitchPosition.AUTO
            if state == LeverState.MIDDLE
            else SwitchPosition.TURNED
        )

    def switch_6_7_action(self, state: LeverState):
        self.window.switch_6_7_controller.set_light(state.value, IndicatorState.ON)
        self.window.switch_6_7.set_position(
            SwitchPosition.Z_DOWN_STRAIGHT
            if state == LeverState.LEFT
            else SwitchPosition.TURNED
            if state == LeverState.MIDDLE
            else SwitchPosition.Z_UP_STRAIGHT
        )

    def switch_8_action(self, state: LeverState):
        self.window.switch_8_controller.set_light(state.value, IndicatorState.ON)
        self.window.switch_8.set_position(
            SwitchPosition.STRAIGHT
            if state == LeverState.LEFT
            else SwitchPosition.AUTO
            if state == LeverState.MIDDLE
            else SwitchPosition.TURNED
        )

    def switch_9_action(self, state: LeverState):
        self.window.switch_9_controller.set_light(state.value, IndicatorState.ON)
        self.window.switch_9.set_position(
            SwitchPosition.STRAIGHT
            if state == LeverState.LEFT
            else SwitchPosition.AUTO
            if state == LeverState.MIDDLE
            else SwitchPosition.TURNED
        )

    def switch_10_action(self, state: LeverState):
        self.window.switch_10_controller.set_light(state.value, IndicatorState.ON)
        self.window.switch_10.set_position(
            SwitchPosition.STRAIGHT
            if state == LeverState.LEFT
            else SwitchPosition.AUTO
            if state == LeverState.MIDDLE
            else SwitchPosition.TURNED
        )

    def check_switch_positions(self):
        self.window.switch_1_3.check_state(True)
        self.window.switch_2.check_state(True)
        self.window.switch_4.check_state(True)
        self.window.switch_5.check_state(True)
        self.window.switch_6_7.check_state(True)
        self.window.switch_8.check_state(True)
        self.window.switch_9.check_state(True)
        self.window.switch_10.check_state(True)

    def revert_switch_positions(self):
        self.window.switch_1_3.check_state()
        self.window.switch_2.check_state()
        self.window.switch_4.check_state()
        self.window.switch_5.check_state()
        self.window.switch_6_7.check_state()
        self.window.switch_8.check_state()
        self.window.switch_9.check_state()
        self.window.switch_10.check_state()

    def run(self):
        self.window.show()
        # self.app.exec_()
