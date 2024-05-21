from queue import Queue
import logging
from PyQt5.QtWidgets import QApplication, QMessageBox

from game.forms.api_package import REStation
from game.data_types.api_package import IndicatorState
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

    def run(self):
        self.window.show()
        self.app.exec_()
