from fastapi import FastAPI, APIRouter
import uvicorn
import logging
import signal
from threading import Thread
from queue import Queue

from utils.api_package import queue_handler
from server.data_types.api_package import StationStatus


class RESTServer:
    rest: FastAPI = FastAPI(title="PyDopSim REST API", version="0.1")
    router: APIRouter = APIRouter()

    def __init__(self, port: int = 8020):
        self.port: int = port
        self.tcp_port: int = 8021

        self.logger = logging.getLogger("App.RESTServer")
        self.logger.setLevel(logging.DEBUG)
        self.logger.info("REST server initialized")
        self.thread_queue: Queue = Queue()
        self.uvicorn_server = None

        self.stations: dict[str:StationStatus] = dict()

    async def root(self) -> dict:
        return {"message": "Welcome to PyDopSim REST API"}

    async def get_stations(self) -> dict:
        return self.stations

    async def get_station(self, station_name: str) -> dict:
        return {
            station_name: self.stations.get(station_name, StationStatus.UNKNOWN.name)
        }

    async def get_available_stations(self) -> dict:
        return {
            station: status.name
            for station, status in self.stations.items()
            if status == StationStatus.OFFLINE
        }

    async def take_station(self, station_name: str) -> dict:
        if self.stations.get(station_name, None) == StationStatus.OFFLINE:
            self.stations[station_name] = StationStatus.ONLINE
            return {"server_tcp_port": self.tcp_port, "server_rest_port": self.port}
        return {"error": "TAKEN"}

    async def release_station(self, station_name: str):
        if self.stations.get(station_name, None) == StationStatus.ONLINE:
            self.stations[station_name] = StationStatus.OFFLINE

    def _assign_routes(self):
        self.router.add_api_route("/", self.root, methods=["GET"])
        self.router.add_api_route("/stations", self.get_stations, methods=["GET"])
        self.router.add_api_route(
            "/stations/{station_name}", self.get_station, methods=["GET"]
        )
        self.router.add_api_route(
            "/available_stations", self.get_available_stations, methods=["GET"]
        )
        self.router.add_api_route(
            "/take_station/{station_name}", self.take_station, methods=["PUT"]
        )
        self.router.add_api_route(
            "/release_station/{station_name}", self.release_station, methods=["PUT"]
        )
        self.rest.include_router(self.router)

    def run(self, port: int = None, tcp_port: int = 8021):
        self._assign_routes()
        if port:
            self.port = port
        self.tcp_port = tcp_port

        self.thread = Thread(target=self.server_thread)
        self.thread.start()

    def add_station(self, station_name: str):
        self.stations[station_name] = StationStatus.AVAILABLE

    def stop(self):
        pass  # TODO: add way to stop the server

    def server_thread(self):
        self.logger.info(f"Starting REST server on port {self.port}")
        rest_logger = logging.getLogger("uvicorn.error")
        rest_logger.addHandler(queue_handler)
        rest_access_logger = logging.getLogger("uvicorn.access")
        rest_access_logger.addHandler(queue_handler)

        uvicorn.run(
            self.rest,
            host="0.0.0.0",
            port=self.port,
            log_level="debug",
            log_config=None,
        )
