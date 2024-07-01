import requests
from queue import Queue
import logging

from game.api_package import REStation
from .logic.api_package import PathBuilder, SignalFinder


class Client:
    def __init__(
        self,
        station_name: str,
        log_pipe: Queue = None,
        allow_debug: bool = False,
        additional_config: dict = None,
    ):
        self.station_name: str = station_name
        self.allow_debug: bool = allow_debug
        self.connection_established: bool = False
        self.host: str = None
        self.port: int = 8021
        self.server_port: int = 8020
        self.additional_config: dict = additional_config

        self.logger = logging.getLogger("App.Client")
        self.logger.setLevel(logging.DEBUG)

        self.relief = REStation(
            station_name=station_name,
            log_pipe=log_pipe,
            button_click_callback=self.build_requested_path,
            button_rightclick_callback=self.cancel_requested_path,
        )
        self.relief._on_exit = self.release_station
        self.path_builder = PathBuilder(relief=self.relief, relief_type="RE")
        self.signal_finder = SignalFinder(relief=self.relief)

        self.first_button_id: str = None
        self.second_button_id: str = None

        if self.allow_debug:
            self.relief.station_button.enable_debug()

    def set_server_info(self, host: str, port: int):
        self.host = host
        self.port = port
        self.logger.debug(f"Server address is set to {host}:{port}")

    def set_rest_port(self, port: int):
        self.server_port: int = port

    def connect(self):
        pass  # TODO: figure out how to connect to the server

    def build_requested_path(self, button_id: str):
        if self.second_button_id is None and self.first_button_id is not None:
            self.second_button_id: str = button_id
        if self.first_button_id is None:
            self.first_button_id: str = button_id

        if self.first_button_id and self.second_button_id:
            self.first_button_id = self.signal_finder.find_signal_by_button(
                self.first_button_id
            )
            self.second_button_id = self.signal_finder.find_signal_by_button(
                self.second_button_id
            )
            self.path_builder.build_path(
                start_signal=self.first_button_id, end_signal=self.second_button_id
            )

            self.first_button_id = None  # reset the buttons
            self.second_button_id = None

    def cancel_requested_path(self, button_id: str):
        signal_id = self.signal_finder.find_signal_by_button(button_id)
        self.path_builder.cancel_path(start_signal=signal_id)

        self.first_button_id = None  # reset the buttons
        self.second_button_id = None
        self.relief.stop_blinking()

    def release_station(self):
        try:
            request = requests.put(
                f"http://{self.host}:{self.server_port}/release_station/{self.station_name}"
            )
            if request.status_code == 200:
                self.logger.info(f"Station {self.station_name} released")

        except Exception as e:
            self.logger.error(f"Failed to release station: {e}")

    def parse_config(self):
        if self.additional_config.get("allow_2L", True) is False:  # allow by default
            self.relief.disable_2L_track()

        if self.additional_config.get("allow_S", True) is False:
            self.relief.disable_S_track()

        if self.additional_config.get("allow_1L", True) is False:
            self.relief.disable_1L_track()

        self.relief.set_left_station_name(
            self.additional_config.get("left_station", self.station_name)
        )
        self.relief.set_right_station_name(
            self.additional_config.get("right_station", self.station_name)
        )
        self.relief.set_turn_station_name(
            self.additional_config.get("turn_station", self.station_name)
        )

    def run(self):
        # put startup code here
        self.logger.info(f"Starting client for {self.station_name}")
        self.parse_config()
        self.relief.show()

    @property
    def connected(self) -> bool:
        return self.connection_established
