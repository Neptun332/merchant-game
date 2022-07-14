from collections import Set

from loguru import logger

from City import City
from Event import Event
from EventEngine import EventEngine
from Map import Map


class GameEngine:

    def __init__(self):
        self.map = Map()
        self.event_engine = EventEngine()
        events = self._create_events_for_cities(self.map.get_cities())

    def run(self):
        logger.info("Started GameEngine")
        self.

    def _create_events_for_cities(self, cities: Set[City]) -> Event:
        return [for city in cities]
