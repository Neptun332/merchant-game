import time

from loguru import logger

from EventEngine import EventEngine
from Map import Map
from TreasureEvent import TreasureEventConfig


class GameEngine:

    def __init__(
            self,
            map: Map,
            event_engine: EventEngine,
            ticks_to_next_month: int,
            tick_rate: float = None,
    ):
        self.tick_rate = tick_rate
        self.map = map
        self.event_engine = event_engine
        self.ticks_to_next_month = ticks_to_next_month
        self.event_engine.create_city_event(
            self.map.cities,
            TreasureEventConfig([200, 300])
        )
        self.tick = 1

    def run(self):
        logger.info("Started GameEngine")
        while True:
            time_at_beginning_of_tick = time.time()

            self._daily_update()
            if self._is_monthly_tick(self.tick):
                self._monthly_update()

            time_at_end_of_tick = time.time()
            if self.tick_rate:
                logger.info("Next real time tick")
                time.sleep(self._calculate_sleep_time_to_next_tick(
                    time_at_beginning_of_tick=time_at_beginning_of_tick,
                    time_at_end_of_tick=time_at_end_of_tick)
                )
            self.tick += 1

    def _daily_update(self):
        self.event_engine.attempt_triggering_events()

    def _monthly_update(self):
        pass

    def _is_monthly_tick(self, tick: int):
        return tick % self.ticks_to_next_month == 0

    def _calculate_sleep_time_to_next_tick(self, time_at_beginning_of_tick: float, time_at_end_of_tick: float):
        return (time_at_beginning_of_tick + (1 / self.tick_rate)) - time_at_end_of_tick
