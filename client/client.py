import socket  # use REST or TCP for the server framework
from queue import Queue

from game.api_package import REStation


class Client:
    def __init__(self, station_name: str, log_pipe: Queue = None):
        self.station_name: str = station_name
        self.host: str = None
        self.port: int = 8040

        self.relief = REStation(station_name=station_name, log_pipe=log_pipe)

    def run(self):
        # put startup code here
        self.relief.show()
