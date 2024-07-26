import os
import signal
import uvicorn
import pandas as pd
from fastapi import FastAPI, APIRouter, Request
from fastapi.responses import JSONResponse, HTMLResponse, FileResponse
from fastapi.exceptions import HTTPException
from fastapi.templating import Jinja2Templates
import logging
import json
from threading import Thread
from queue import Queue
from uuid import uuid4

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
        with sqlite_handler.get_connection() as conn:
            station_df = pd.read_sql("SELECT * FROM stations", conn)
            station_df.rename(
                columns={
                    "station_name": "Názov stanice",
                    "status": "Stav",
                    "station_type": "Typ stanice",
                    "player_name": "Hráč",
                    "left_station": "Ľavá stanica",
                    "right_station": "Pravá stanica",
                    "turn_station": "Stanica v odbočke",
                },
                inplace=True,
            )
            station_df.drop(columns=["uid"], inplace=True)
            station_df.replace({None: "-"}, inplace=True)
            station_df["Trať"] = station_df["route_uid"].apply(
                lambda x: conn.execute(
                    f"SELECT route_name FROM routes WHERE uid = '{x}';"
                ).fetchone()[0]
            )
            station_df.drop(columns=["route_uid", "station_inflections"], inplace=True)

            train_df = pd.read_sql("SELECT * FROM trains", conn)
            train_df.rename(
                columns={
                    "train_number": "Číslo vlaku",
                    "train_type": "Typ vlaku",
                    "origin_station": "Počiatočná stanica",
                },
                inplace=True,
            )
            train_df.drop(columns=["uid"], inplace=True)
            train_df["Trať"] = train_df["route_uid"].apply(
                lambda x: conn.execute(
                    f"SELECT route_name FROM routes WHERE uid = '{x}';"
                ).fetchone()[0]
            )
            train_df.drop(columns=["route_uid"], inplace=True)
            train_df["Počiatočná stanica"] = train_df["Počiatočná stanica"].apply(
                lambda x: conn.execute(
                    f"SELECT station_name FROM stations WHERE uid = '{x}';"
                ).fetchone()[0]
            )
            train_df = train_df[
                ["Typ vlaku", "Číslo vlaku", "Počiatočná stanica", "Trať"]
            ]  # reorder columns

            route_df = pd.read_sql("SELECT * FROM routes", conn)

        return self.templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "table_html": station_df.to_html(index=False, table_id="station_table"),
                "table_html_trains": train_df.to_html(
                    index=False, table_id="train_table"
                ),
                "routes": route_df["route_name"].to_list(),
            },
        )

    async def get_file(self, filename: str) -> FileResponse:
        return FileResponse(f"{assets_path}/{filename}")

    async def get_stations(self) -> JSONResponse:
        with sqlite_handler.get_connection() as con:
            stations: pd.DataFrame = pd.read_sql_query("SELECT * FROM stations", con)
            stations["route"] = stations["route_uid"].apply(
                lambda x: con.execute(
                    f"SELECT route_name FROM routes WHERE uid = '{x}';"
                ).fetchone()[0]
            )
            stations.drop(
                columns=["uid", "route_uid", "station_inflections"], inplace=True
            )
            stations.replace({None: "-"}, inplace=True)

            return json.loads(
                str(stations.to_dict(orient="records"))
                .replace("'", '"')
                .encode("utf-8")
            )

    async def get_station(self, station_name: str) -> dict:
        with sqlite_handler.get_cursor() as curr:
            curr.execute(
                f"SELECT * FROM stations WHERE station_name = '{station_name}';"
            )
            station = curr.fetchone()

            if station:
                return {
                    "station_name": station[1],
                    "status": station[6],
                    "station_type": station[5],
                    "player_name": station[7],
                    "left_station": station[2],
                    "right_station": station[3],
                    "turn_station": station[4],
                    "route": curr.execute(
                        f"SELECT route_name FROM routes WHERE uid = '{station[8]}';"
                    ).fetchone()[0],
                }
            return {"error": "Station not found"}

    async def get_available_stations(self) -> JSONResponse:
        with sqlite_handler.get_connection() as curr:
            stations_df = pd.read_sql(
                "SELECT * FROM stations WHERE stations.status == 'OFFLINE'", curr
            )
            stations_df.drop(
                columns=[
                    "uid",
                    "station_inflections",
                    "left_station",
                    "right_station",
                    "turn_station",
                    "player_name",
                ],
                inplace=True,
            )
            stations_df["route"] = stations_df["route_uid"].apply(
                lambda x: curr.execute(
                    f"SELECT route_name FROM routes WHERE uid = '{x}';"
                ).fetchone()[0]
            )
            stations_df.drop(columns=["route_uid"], inplace=True)

            return json.loads(
                str(stations_df.to_dict(orient="records"))
                .replace("'", '"')
                .encode("utf-8")
            )

    async def register_train(
        self, train_id: str, train_type: TrainType, origin_station: str
    ) -> JSONResponse:
        with sqlite_handler.get_cursor() as curr:
            curr.execute(
                f"SELECT EXISTS(SELECT 1 FROM stations WHERE station_name = '{origin_station}');"
            )
            if curr.fetchone()[0] == 0:
                return {"error": "Station not found"}

            curr.execute(
                f"SELECT EXISTS(SELECT 1 FROM trains WHERE train_number = '{train_id}');"
            )
            if curr.fetchone()[0] == 1:
                return {
                    "error": "Train already registered"
                }  # TODO: for now there cant be train with same number in multiple routes

            curr.execute(
                f"INSERT INTO trains (uid, train_number, train_type, origin_station, route_uid) VALUES ('{str(uuid4())}','{train_id}', '{train_type.name}', (SELECT uid FROM stations WHERE station_name = '{origin_station}'), (SELECT route_uid FROM stations WHERE station_name = '{origin_station}'));"
            )
            return {
                "message": f"Train {train_type.value} {train_id} registered successfully"
            }

    async def remove_train(self, train_id: str) -> JSONResponse:
        with sqlite_handler.get_cursor() as curr:
            curr.execute(
                f"SELECT EXISTS(SELECT 1 FROM trains WHERE train_number = '{train_id}');"
            )
            if curr.fetchone()[0] == 0:
                return {"error": "Train not found"}

            curr.execute(f"DELETE FROM trains WHERE train_number = '{train_id}';")
            return {"message": f"Train {train_id} removed successfully"}

    async def modify_train(
        self, train_id: str, train_type: TrainType, new_number: int
    ) -> JSONResponse:
        with sqlite_handler.get_cursor() as curr:
            curr.execute(
                f"SELECT EXISTS(SELECT 1 FROM trains WHERE train_number = '{train_id}');"
            )
            if curr.fetchone()[0] == 0:
                return {"error": "Train not found"}

            curr.execute(
                f"UPDATE trains SET train_number = '{new_number}', train_type = '{train_type.name}' WHERE train_number = '{train_id}';"
            )
            return {
                "message": f"Train {train_id} modified successfully to {train_type.value} {new_number}"
            }

    async def take_station(self, station_name: str, client_name: str) -> JSONResponse:
        with sqlite_handler.get_cursor() as curr:
            curr.execute(
                f"SELECT * FROM stations WHERE station_name = '{station_name}';"
            )
            station = curr.fetchone()
            if station:
                if station[6] == StationStatus.OFFLINE.value:
                    curr.execute(
                        f"UPDATE stations SET status = '{StationStatus.ONLINE.value}', player_name = '{client_name}' WHERE station_name = '{station_name}';"
                    )
                    return_dict: dict = {
                        "server_tcp_port": self.tcp_port,
                        "server_rest_port": self.port,
                    }
                    return_dict.update(
                        {
                            "station_name": station[1],
                            "status": station[6],
                            "station_type": station[5],
                            "player_name": station[7],
                            "left_station": station[2],
                            "right_station": station[3],
                            "turn_station": station[4],
                            "route": curr.execute(
                                f"SELECT route_name FROM routes WHERE uid = '{station[8]}';"
                            ).fetchone()[0],
                        }
                    )
                    return return_dict
                return {"error": "TAKEN"}
            raise HTTPException(status_code=404, detail="Station not found")

    async def release_station(self, station_name: str) -> JSONResponse:
        with sqlite_handler.get_cursor() as curr:
            curr.execute(
                f"SELECT * FROM stations WHERE station_name = '{station_name}';"
            )
            station = curr.fetchone()
            if station:
                if station[6] == StationStatus.ONLINE.value:
                    curr.execute(
                        f"UPDATE stations SET status = '{StationStatus.OFFLINE.value}', player_name = NULL WHERE station_name = '{station_name}';"
                    )
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
