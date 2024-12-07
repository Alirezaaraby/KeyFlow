from exceptions.storage_exceptions import StorageException
from tinydb import TinyDB
from core.db import DBAdapter
from os.path import join

class TinydbAdapter(DBAdapter):

    DATABASE_NAME = "keyflow.json"

    def __init__(self, path):
        try:
            self.db = TinyDB(join(path, self.DATABASE_NAME))
        except Exception as e:
            raise StorageException(f"Failed to initialize TinyDB: {e}")

    def save_event(self, data):
        try:
            self.db.insert(data)
        except Exception as e:
            raise StorageException(f"Failed to save event: {e}")
