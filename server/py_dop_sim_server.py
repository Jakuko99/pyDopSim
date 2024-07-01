import logging


from .tcp_server.api_package import TCPServer
from .rest_server.api_package import RESTServer


class PyDopSimServer:
    def __init__(self):
        self.host: str = None
        self.rest_port: int = 8020
        self.port: int = 8021
        self.running: bool = False

        self.logger = logging.getLogger("App.Server")
        self.logger.setLevel(logging.DEBUG)

        self.logger.info("PyDopSimServer initialized")
        self.rest = RESTServer(self.rest_port)
        self.tcp = TCPServer(port=self.port)

    def set_ports(self, rest_port: int, tcp_port: int):
        self.logger.debug(
            f"Setting REST port to {rest_port} and TCP port to {tcp_port}"
        )
        self.rest_port = rest_port
        self.port = tcp_port

    def add_station_dict(self, stations: dict):
        self.logger.debug(f"Adding {len(stations)} stations to the server")
        self.rest.stations = stations

    def run(self):
        self.running = True
        self.rest.run(port=self.rest_port, tcp_port=self.port)
        self.tcp.start(port=self.port)

    def stop(self):
        self.running = False
        self.rest.stop()
        self.tcp.stop()
