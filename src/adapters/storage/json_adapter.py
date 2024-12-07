import json
from datetime import datetime
from core.db import DBAdapter
from os.path import join, dirname
from os import makedirs
from exceptions.storage_exceptions import (
    StoragePermissionException,
    StorageNotFoundException,
    StorageParserException,
    StorageOSException,
    StorageIOErrorException,
)

class JSONAdapter(DBAdapter):
    DATABASE_NAME = "keyflow.json"

    def __init__(self, path, **kwargs):
        self.file_path = join(path, self.DATABASE_NAME)

    def save_event(self, data):
        log_entry = {
            "keys": data["keys"],
            "timestamp": datetime.now().isoformat()
        }
        try:
            directory = dirname(self.file_path)
            if directory:
                makedirs(directory, exist_ok=True)

            with open(self.file_path, "a") as f:
                f.write(json.dumps(log_entry) + "\n")
        except PermissionError:
            raise StoragePermissionException(f"Insufficient permissions to write to {self.file_path}.")
        except FileNotFoundError:
            raise StorageNotFoundException(f"Directory not found for the file path: {self.file_path}.")
        except OSError as e:
            raise StorageOSException(f"OS error occurred: {e}")
        except TypeError as e:
            raise StorageParserException(f"Failed to serialize the log entry to JSON: {e}")
        except IOError as e:
            raise StorageIOErrorException(f"Failed to save event due to an IO error: {e}")
