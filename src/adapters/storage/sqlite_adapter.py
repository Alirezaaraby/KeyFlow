import sqlite3
from core.db import DBAdapter
from datetime import datetime
from os.path import join, dirname
from os import makedirs
from threading import Lock
from exceptions.storage_exceptions import (
    StoragePermissionException,
    StorageNotFoundException,
    StorageParserException,
    StorageOSException,
    StorageIOErrorException,
)

class SQLiteAdapter(DBAdapter):
    
    DATABASE_NAME = "keyflow.db"

    def __init__(self, path):
        try:
            
            directory = dirname(join(path, self.DATABASE_NAME))
            if directory:
                makedirs(directory, exist_ok=True)

            self.connection = sqlite3.connect(
                join(path, self.DATABASE_NAME), check_same_thread=False
            )
            self.cursor = self.connection.cursor()
            self.lock = Lock()

            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS keyflow (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    keys TEXT,
                    timestamp TEXT
                )
            """)
            self.connection.commit()

        except PermissionError:
            raise StoragePermissionException(f"Insufficient permissions to access {path}.")
        except FileNotFoundError:
            raise StorageNotFoundException(f"Directory not found for the path: {path}.")
        except sqlite3.OperationalError as e:
            raise StorageOSException(f"SQLite operational error: {e}")
        except sqlite3.DatabaseError as e:
            raise StorageIOErrorException(f"SQLite database error: {e}")
        except OSError as e:
            raise StorageOSException(f"OS error occurred while initializing SQLite: {e}")

    def save_event(self, data):
        try:
            with self.lock:
                self.cursor.execute(
                    "INSERT INTO keyflow (keys, timestamp) VALUES (?, ?)", 
                    (",".join(data["keys"]), datetime.now().isoformat())
                )
                self.connection.commit()

        except sqlite3.OperationalError as e:
            raise StorageOSException(f"SQLite operational error while saving event: {e}")
        except sqlite3.IntegrityError as e:
            raise StorageIOErrorException(f"SQLite integrity error: {e}")
        except sqlite3.DatabaseError as e:
            raise StorageIOErrorException(f"SQLite database error while saving event: {e}")
        except TypeError as e:
            raise StorageParserException(f"Non-serializable data provided for saving event: {e}")
        except OSError as e:
            raise StorageOSException(f"OS error occurred while saving data to SQLite: {e}")
        except IOError as e:
            raise StorageIOErrorException(f"I/O error occurred while saving data to SQLite: {e}")
