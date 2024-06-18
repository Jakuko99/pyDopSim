import socket  # use REST or TCP for the server framework
from queue import Queue
import logging

from game.api_package import REStation
from .logic.api_package import PathBuilder, SignalFinder


class Client:
    def __init__(
        self, station_name: str, log_pipe: Queue = None, allow_debug: bool = False
    ):
        self.station_name: str = station_name
        self.allow_debug: bool = allow_debug
        self.connection_established: bool = False
        self.host: str = None
        self.port: int = 8040

        self.logger = logging.getLogger("App.Client")
        self.logger.setLevel(logging.DEBUG)

        self.relief = REStation(
            station_name=station_name,
            log_pipe=log_pipe,
            button_click_callback=self.build_requested_path,
            button_rightclick_callback=self.cancel_requested_path,
        )
        self.path_builder = PathBuilder(relief=self.relief, relief_type="RE")
        self.signal_finder = SignalFinder(relief=self.relief)

        self.first_button_id: str = None
        self.second_button_id: str = None

        if self.allow_debug:
            self.relief.station_button.enable_debug()

    def set_server_info(self, host: str, port: int):
        self.host = host
        self.port = port
        self.logger.debug(f"Server info is set to {host}:{port}")

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

    def run(self):
        # put startup code here
        self.logger.info(f"Starting client for {self.station_name}")
        self.relief.show()

    @property
    def connected(self) -> bool:
        return self.connection_established
