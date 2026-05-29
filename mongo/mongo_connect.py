from pymongo import MongoClient
import logging

logger = logging.getLogger(__name__)

class MONGO_DB_CONNECT():
    def __init__(self):
        self._client  = MongoClient("mongodb+srv://ikorcagin11_db_user:1029384756Ivan!@cluster0.tjx2czc.mongodb.net/")

    def __enter__(self):
        self.mongo_db = self._client['sakila_analytics']
        logger.info("Подключино к mongodb")
        return self.mongo_db

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._client.close()
        logger.info("отключино от mongodb")

with MONGO_DB_CONNECT() as mongo_db:
    collection = mongo_db['sakila_film']





