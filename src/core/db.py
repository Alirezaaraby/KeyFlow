from abc import ABC, abstractmethod

class DBAdapter(ABC):
    @abstractmethod
    def save_event(self, data):
        pass
