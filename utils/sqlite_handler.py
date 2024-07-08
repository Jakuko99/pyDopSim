import logging
import sqlite3
from contextlib import contextmanager


class SqliteHandler:
    def __init__(self, db_path: str):
        self.logger = logging.getLogger("App.Server.SqliteHandler")
        self.logger.setLevel(logging.DEBUG)
        self.logger.info(f"Initializing SqliteHandler with database at {db_path}")

        try:
            self.conn: sqlite3.Connection = sqlite3.connect(db_path)
        except sqlite3.Error as e:
            self.logger.error(e)

    @contextmanager
    def get_cursor(self):
        cursor: sqlite3.Cursor = self.conn.cursor()
        try:
            yield cursor
            self.conn.commit()
        except sqlite3.Error as e:
            self.logger.error(e)
            self.conn.rollback()
        finally:
            cursor.close()


sqlite_handler = SqliteHandler("pydopsim.db")  # singleton for database connection
