from abc import ABC, abstractmethod


class Event(ABC):

    @abstractmethod
    def handle(self):
        pass

    @abstractmethod
    def get_message(self):
        pass
