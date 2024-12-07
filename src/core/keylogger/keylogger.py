from pynput import keyboard
from exceptions.keylogger_exceptions import (
    KeyloggerPermissionException,
    KeyloggerOSException,
    KeyloggerQueueException,
    KeyloggerUnexpectedException,
)

class Keylogger:
    def __init__(self, queue):
        self.queue = queue
        self.current_keys = set()

    def on_press(self, key):
        try:
            if hasattr(key, 'char') and key.char.isprintable():
                self.current_keys.add(key.char)
            else:
                self.current_keys.add(str(key))
        except AttributeError:
            raise KeyloggerUnexpectedException("Failed to process key attribute.")
        except Exception as e:
            raise KeyloggerUnexpectedException(f"Unexpected error: {e}")

    def on_release(self, key):
        try:
            self.queue.put({"keys": list(self.current_keys)})
            self.current_keys.clear()
            if key == keyboard.Key.esc:
                return False
        except AttributeError:
            raise KeyloggerUnexpectedException("Failed to process key attribute.")
        except Exception as e:
            raise KeyloggerQueueException(f"Queue operation error: {e}")

    def start(self):
        try:
            with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
                listener.join()
        except PermissionError:
            raise KeyloggerPermissionException()
        except OSError as e:
            raise KeyloggerOSException(f"OS-level error: {e}")
        except Exception as e:
            raise KeyloggerUnexpectedException(f"Unexpected error: {e}")
