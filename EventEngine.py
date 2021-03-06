import random
from decimal import Decimal
from typing import List

from City import City
from TreasureEvent import TreasureEvent, Percentage, TreasureEventConfig


class EventEngine:

    def __init__(self):
        self.city_events_types = [TreasureEvent]
        self.kingdom_events_types = []
        self.events_types = self.city_events_types + self.kingdom_events_types
        self.events = []

    def create_city_event(
            self, cities: List[City],
            treasury_event_config: TreasureEventConfig
    ):
        self.events += [
            event_type(city, treasury_event_config)
            for event_type in self.city_events_types
            for city in cities
        ]

    def attempt_triggering_events(self):
        for event in self.events:
            if self._get_random_percentage().value <= event.calculate_probability():
                event.handle()

    def _get_random_percentage(self) -> Percentage:
        return Percentage(Decimal(random.uniform(Percentage.MIN, Percentage.MAX)))
