import socket
import logging


class TCPServer:
    def __init__(self, host: str = "0.0.0.0", port: int = 8021):
        self.host: str = host
        self.port: int = port

        self.logger = logging.getLogger("App.Server.TCP")
        self.logger.setLevel(logging.DEBUG)

    def start(self, port: int = 8021):
        self.port = port

    def stop(self):
        pass
