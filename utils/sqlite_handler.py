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
            self.conn: sqlite3.Connection = sqlite3.connect(db_path)
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
                "uuid"	STR,
                "station_name"	STR,
                "left_station"	STR,
                "right_station"	STR,
                "turn_station"	STR,
                "station_type"	STR,
                "status"	STR,
                "station_name_N"	INTEGER,
                "station_name_G"	INTEGER,
                "station_name_L"	INTEGER,
                "player_name"	INTEGER,
                PRIMARY KEY("uuid")
                );
            """
            )
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS "servers" (
                server_id INTEGER PRIMARY KEY,
                server_ip STR,
                server_port INTEGER
                );
                """
            )
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS "trains"(
                "uuid"	STR,
                "train_number" INTEGER,
                "train_type"	STR,
                "origin_station"	STR,
                PRIMARY KEY("uuid"),
                FOREIGN KEY("origin_station") REFERENCES "stations"("uuid")
                );
                """
            )

        self.logger.info("Database tables created")


sqlite_handler = SqliteHandler("pydopsim.db")  # singleton for database connection
