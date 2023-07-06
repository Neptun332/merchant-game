import random
from typing import List, Tuple

from Probability import Probability
from event_engine.Event import Event
from event_engine.IEventEngine import IEventEngine


class EventEngine(IEventEngine):

    def __init__(self):
        self.events = []

    def register_possible_event(self, events: List[Tuple[Event, Probability]]):
        self.events += events

    def update(self):
        self.attempt_triggering_events()

    def attempt_triggering_events(self):
        not_handled_events = []
        for event in self.events:
            if self._get_random_propability() <= event.get_probability():
                event.handle()
            else:
                not_handled_events.append(event)
        self.events = not_handled_events

    def _get_random_propability(self) -> Probability:
        return Probability(random.uniform(Probability.MIN, Probability.MAX))
