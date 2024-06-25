import socket


class TCPServer:
    def __init__(self, host: str, port: int = 8021):
        self.host: str = host
        self.port: int = port
