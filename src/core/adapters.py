from adapters.storage.json_adapter import JSONAdapter
from adapters.storage.tinydb_adapter import TinydbAdapter
from adapters.storage.sqlite_adapter import SQLiteAdapter

database_adapters = {
    "json": JSONAdapter,
    "tinydb": TinydbAdapter,
    "sqlite": SQLiteAdapter,
}