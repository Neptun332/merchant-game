from abc import abstractmethod, ABC
from typing import List, Tuple

from Probability import Probability
from event_engine.Event import Event


class IEventEngine(ABC):
    @abstractmethod
    def register_possible_event(self, events: List[Event]):
        ...

    @abstractmethod
    def update(self):
        ...

    @abstractmethod
    def attempt_triggering_events(self):
        ...
