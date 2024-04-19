import socket


class PyDopSimServer:
    def __init__(self, host: str, port: int = 8088):
        self.host: str = host
        self.port: int = port
