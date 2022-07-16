import time

from loguru import logger

from EventEngine import EventEngine
from Map import Map
from TreasureEvent import TreasureEventConfig


class GameEngine:

    def __init__(self, tick_rate: float = None):
        self.tick_rate = tick_rate
        self.map = Map()
        self.event_engine = EventEngine()
        self.event_engine.create_city_event(
            self.map.cities,
            TreasureEventConfig([200, 300])
        )

    def run(self):
        logger.info("Started GameEngine")
        while True:
            time_at_beginning_of_tick = time.time()

            self.event_engine.attempt_triggering_events()

            time_at_end_of_tick = time.time()
            if self.tick_rate:
                logger.info("Next real time tick")
                time.sleep(self._calculate_sleep_time_to_next_tick(
                    time_at_beginning_of_tick=time_at_beginning_of_tick,
                    time_at_end_of_tick=time_at_end_of_tick)
                )

    def _calculate_sleep_time_to_next_tick(self, time_at_beginning_of_tick: float, time_at_end_of_tick: float):
        return (time_at_beginning_of_tick + (1 / self.tick_rate)) - time_at_end_of_tick
