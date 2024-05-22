from queue import Queue
import logging
from PyQt5.QtWidgets import QApplication, QMessageBox

from game.forms.api_package import REStation
from game.data_types.api_package import IndicatorState, TrackState
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

    def add_test_bindings(self):
        self.window.path_build_cancel.setFunctions(
            lambda: self.window.path_build.set_state(IndicatorState.ON),  # left click
            lambda: self.window.path_build.set_state(IndicatorState.OFF),  # right click
            lambda: self.window.path_build.set_state(
                IndicatorState.BLINKING
            ),  # middle click
        )
        self.window.switch_1_3.set_update_function(
            lambda state: self.window.switch_1_3.set_light(
                state.value, IndicatorState.ON
            )
        )
        self.window.switch_2.set_update_function(
            lambda state: self.window.switch_2.set_light(state.value, IndicatorState.ON)
        )
        self.window.switch_4_vk2.set_update_function(
            lambda state: self.window.switch_4_vk2.set_light(
                state.value, IndicatorState.ON
            )
        )
        self.window.switch_5.set_update_function(
            lambda state: self.window.switch_5.set_light(state.value, IndicatorState.ON)
        )
        self.window.vk_1.set_update_function(
            lambda state: self.window.vk_1.set_light(state.value, IndicatorState.ON)
        )
        self.window.switch_6_7.set_update_function(
            lambda state: self.window.switch_6_7.set_light(
                state.value, IndicatorState.ON
            )
        )
        self.window.switch_8.set_update_function(
            lambda state: self.window.switch_8.set_light(state.value, IndicatorState.ON)
        )
        self.window.switch_9.set_update_function(
            lambda state: self.window.switch_9.set_light(state.value, IndicatorState.ON)
        )
        self.window.switch_10.set_update_function(
            lambda state: self.window.switch_10.set_light(
                state.value, IndicatorState.ON
            )
        )

        self.window.track_1.click_callaback = self.track1_callback
        self.window.track_2.click_callaback = self.track2_callback
        self.window.track_3.click_callaback = self.track3_callback
        self.window.track_5.click_callaback = self.track5_callback
        self.window.track_4.click_callaback = self.track4_callback
        self.window.track_4.right_click_callback = (
            lambda x: self.window.track_4.set_state(TrackState.FREE)
        )

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

    def run(self):
        self.window.show()
        self.app.exec_()
