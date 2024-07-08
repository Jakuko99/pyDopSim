import logging
import sqlite3
from contextlib import contextmanager


class SqliteHandler:
    def __init__(self, db_path: str):
        self.logger = logging.getLogger("App.Server.SqliteHandler")
        self.logger.setLevel(logging.DEBUG)
        self.logger.info("Initializing SqliteHandler")

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

if __name__ == "__main__":  # test script
    import pandas as pd

    with sqlite_handler.get_cursor() as c:
        df = pd.read_sql_query("SELECT * FROM stations", c.connection)
        print(df)
