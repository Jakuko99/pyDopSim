import logging
import sqlite3
from contextlib import contextmanager
from typing import Iterator


class SqliteHandler:
    def __init__(self, db_path: str):
        self.logger = logging.getLogger("App.Server.SqliteHandler")
        self.logger.setLevel(logging.DEBUG)
        self.logger.info("Initializing SqliteHandler")

        try:
            self.conn: sqlite3.Connection = sqlite3.connect(
                db_path, check_same_thread=False
            )
        except sqlite3.Error as e:
            self.logger.error(e)

        with self.get_cursor() as cursor:
            cursor.execute(
                'SELECT EXISTS(SELECT 1 FROM sqlite_master WHERE type="table" AND name="trains");'
            )
            res = cursor.fetchone()
            if res[0] == 0:
                self.create_tables()

    @contextmanager
    def get_cursor(self) -> Iterator[sqlite3.Cursor]:
        cursor: sqlite3.Cursor = self.conn.cursor()
        try:
            yield cursor
            self.conn.commit()
        except sqlite3.Error as e:
            self.logger.error(e)
            self.conn.rollback()
        finally:
            cursor.close()

    @contextmanager
    def get_connection(self) -> Iterator[sqlite3.Connection]:
        cursor: sqlite3.Cursor = self.conn.cursor()
        try:
            yield cursor.connection
            self.conn.commit()
        except sqlite3.Error as e:
            self.logger.error(e)
            self.conn.rollback()
        finally:
            cursor.close()

    def create_tables(self):
        with self.get_cursor() as cursor:
            cursor.execute(
                """
               CREATE TABLE IF NOT EXISTS "stations" (
                "uid"	STR,
                "station_name"	STR,
                "left_station"	STR,
                "right_station"	STR,
                "turn_station"	STR,
                "station_type"	STR,
                "status"	STR,
                "player_name"	STR,
                "route_uid"	STR,
                "station_inflections"	STR,
                FOREIGN KEY("route_uid") REFERENCES "routes"("uid"),
                FOREIGN KEY("station_inflections") REFERENCES "station_names"("station_name"),
                PRIMARY KEY("uid")
                );
            """
            )
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS "servers" (
                server_id INTEGER,
                server_ip STR,
                server_port INTEGER,
                PRIMARY KEY("server_id" AUTOINCREMENT)
                );
                """
            )
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS "trains"(
                "uid"	STR,
                "train_number" INTEGER,
                "train_type"	STR,
                "origin_station"	STR,
                "route_uid"	STR,
                PRIMARY KEY("uid"),
                FOREIGN KEY("origin_station") REFERENCES "stations"("uid"),
                FOREIGN KEY("route_uid") REFERENCES "routes"("uid")
                );
                """
            )
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS "station_names"(
                "station_name"	STR,
                "station_name_N"	STR,
                "station_name_G"	STR,
                "station_name_L"	STR,
                PRIMARY KEY("station_name")
                );
                """
            )
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS "routes"(
                "uid"	STR,
                "route_name"	STR,
                PRIMARY KEY("uid")
                );
                """
            )

        self.logger.info("Database tables created")


sqlite_handler = SqliteHandler("pydopsim.db")  # singleton for database connection
