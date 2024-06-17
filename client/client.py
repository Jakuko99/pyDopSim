import socket  # use REST or TCP for the server framework
from queue import Queue

from game.api_package import REStation


class Client:
    def __init__(
        self, station_name: str, log_pipe: Queue = None, allow_debug: bool = False
    ):
        self.station_name: str = station_name
        self.allow_debug: bool = allow_debug
        self.connection_established: bool = False
        self.host: str = None
        self.port: int = 8040

        self.relief = REStation(station_name=station_name, log_pipe=log_pipe)
        if self.allow_debug:
            self.relief.station_button.enable_debug()

    def set_server_info(self, host: str, port: int):
        self.host = host
        self.port = port

    def connect(self):
        pass  # TODO: figure out how to connect to the server

    def run(self):
        # put startup code here
        self.relief.show()

    @property
    def connected(self) -> bool:
        return self.connection_established
