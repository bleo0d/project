import os
import pymysql
from dotenv import load_dotenv
import logging

logger = logging.getLogger(__name__)


load_dotenv()

class SQL_DB_CONNECT:
    def __init__(self):
        self._config = {
            "host": os.getenv("SQL_DB_HOST"),
            "user": os.getenv("SQL_DB_USER"),
            "password": os.getenv("SQL_DB_PASSWORD"),
            "database": os.getenv("SQL_DB_NAME")
        }

    def __enter__(self):
        self.conn = pymysql.connect(**self._config)
        self.cursor = self.conn.cursor()
        logger.info("подключено к серверу")
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.conn.close()
        logger.info("выход из сервера")
        return False

    def _execute(self, sql, params=None):
        self.cursor.execute(sql, params)
        return self.cursor.fetchall()

    def _commit(self):
        self.conn.commit()