import socket


class Client:
    def __init__(self, server_ip: str, server_port: int = 8088):
        self.host = server_ip
        self.port = server_port
