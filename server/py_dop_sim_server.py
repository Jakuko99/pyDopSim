import logging


from .tcp_server.api_package import TCPServer
from .rest_server.api_package import RESTServer


class PyDopSimServer:
    def __init__(self):
        self.host: str = None
        self.rest_port: int = 8020
        self.port: int = None

        self.logger = logging.getLogger("App.PyDopSimServer")
        self.logger.setLevel(logging.DEBUG)

        self.logger.info("PyDopSimServer initialized")
        self.rest = RESTServer(self.rest_port)

    def run(self):
        self.rest.run()
