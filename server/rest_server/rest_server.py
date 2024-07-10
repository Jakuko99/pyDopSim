import os
import signal
import uvicorn
import pandas as pd
from fastapi import FastAPI, APIRouter, Request
from fastapi.responses import JSONResponse, HTMLResponse, FileResponse
from fastapi.exceptions import HTTPException
from fastapi.templating import Jinja2Templates
import logging
from threading import Thread
from queue import Queue

from utils.api_package import queue_handler
from server.data_types.api_package import StationStatus
from game.data_types.api_package import TrainType
from server.objects.api_package import Station
from utils.api_package import sqlite_handler

rest_path = f"{os.path.dirname(os.path.abspath(__file__))}"
assets_path = rest_path.replace(r"server\rest_server", "assets")


class RESTServer:
    rest: FastAPI = FastAPI(title="PyDopSim REST API", version="0.1")
    router: APIRouter = APIRouter()

    def __init__(self, port: int = 8020):
        self.port: int = port
        self.tcp_port: int = 8021

        self.logger = logging.getLogger("App.Server.REST")
        self.logger.setLevel(logging.DEBUG)
        self.logger.info("REST server initialized")
        self.thread_queue: Queue = Queue()
        self.uvicorn_server = None
        self.templates = Jinja2Templates(directory=f"{rest_path}/templates")

        self.stations: dict[str:Station] = dict()

    async def root(self, request: Request) -> HTMLResponse:
        table_columns = [
            "Názov stanice",
            "Stav",
            "Typ stanice",
            "Hráč",
            "Ľavá stanica",
            "Pravá stanica",
            "Stanica v odbočke",
            "Trať",
        ]
        table_rows = []
        with sqlite_handler.get_connection() as conn:
            station_df = pd.read_sql("SELECT * FROM stations", conn)
        for _, station in station_df.iterrows():
            row = [
                station["station_name"],
                station["status"],
                station["station_type"],
                station["player_name"],
                station["left_station"],
                station["right_station"],
                station["turn_station"],
                conn.execute(
                    f"SELECT route_name FROM routes WHERE uid = '{station['route_uid']}';"
                ).fetchone()[0],
            ]
            table_rows.append(["-" if item is None else item for item in row])
        df = pd.DataFrame(table_rows, columns=table_columns)

        return self.templates.TemplateResponse(
            "index.html", {"request": request, "table_html": df.to_html(index=False)}
        )

    async def get_file(self, filename: str) -> FileResponse:
        return FileResponse(f"{assets_path}/{filename}")

    async def get_stations(self) -> dict:
        return {name: station.__dict__ for name, station in self.stations.items()}

    async def get_station(self, station_name: str) -> dict:
        station: Station = self.stations.get(station_name, None)
        if station:
            return {station_name: station.__dict__}

    async def get_available_stations(self) -> dict:
        return {
            station_name: station.status.name
            for station_name, station in self.stations.items()
            if station.status == StationStatus.OFFLINE
        }

    async def register_train(
        self, train_id: str, train_type: TrainType, origin_station: str
    ) -> JSONResponse:
        raise HTTPException(status_code=501, detail="Not implemented")

    async def remove_train(self, train_id: str) -> JSONResponse:
        raise HTTPException(status_code=501, detail="Not implemented")

    async def modify_train(
        self, train_id: str, train_type: TrainType, new_number: int
    ) -> JSONResponse:
        raise HTTPException(status_code=501, detail="Not implemented")

    async def take_station(self, station_name: str, client_name: str) -> JSONResponse:
        if self.stations.get(station_name, None):
            if self.stations.get(station_name).status == StationStatus.OFFLINE:
                self.stations[station_name].status = StationStatus.ONLINE
                self.stations[station_name].player_name = client_name
                return_dict: dict = {
                    "server_tcp_port": self.tcp_port,
                    "server_rest_port": self.port,
                }
                return_dict.update(self.stations[station_name].__dict__)
                return return_dict
            return {"error": "TAKEN"}
        raise HTTPException(status_code=404, detail="Station not found")

    async def release_station(self, station_name: str) -> JSONResponse:
        if self.stations.get(station_name, None):
            if self.stations.get(station_name, None).status == StationStatus.ONLINE:
                self.stations[station_name].status = StationStatus.OFFLINE
                self.stations[station_name].player_name = None
                return {"message": "Station released successfully"}
            return {"error": "Station not taken"}
        raise HTTPException(status_code=404, detail="Station not found")

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
        self.router.add_api_route(
            "/register_train/{train_id}",
            self.register_train,
            methods=["POST"],
        )
        self.router.add_api_route(
            "/modify_train/{train_id}",
            self.modify_train,
            methods=["PUT"],
        )
        self.router.add_api_route(
            "/remove_train/{train_id}",
            self.remove_train,
            methods=["DELETE"],
        )
        self.router.add_api_route("/assets/{filename}", self.get_file, methods=["GET"])
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
        os.kill(os.getpid(), signal.SIGINT)  # kills entire program

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
