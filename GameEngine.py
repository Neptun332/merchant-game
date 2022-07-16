from collections import Set

from loguru import logger

from City import City
from Event import Event
from EventEngine import EventEngine
from Map import Map
from TreasureEvent import TreasureEventConfig


class GameEngine:

    def __init__(self):
        self.map = Map()
        self.event_engine = EventEngine()
        self.event_engine.create_city_event(
            self.map.cities,
            TreasureEventConfig([200, 300])
        )

    def run(self):
        logger.info("Started GameEngine")
        while True:
            self.event_engine.attempt_triggering_events()

