from abc import ABC, abstractmethod
from enum import Enum, auto


class EventStateEnum(Enum):
    NOT_TRIGGERED = auto()
    TRIGGERED = auto()


class Event(ABC):
    state = EventStateEnum.NOT_TRIGGERED

    @abstractmethod
    def handle(self):
        pass

    @abstractmethod
    def get_message(self):
        pass

    @abstractmethod
    def calculate_probability(self):
        pass
