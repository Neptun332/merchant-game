import time

from loguru import logger
from matplotlib import pyplot as plt

from EventEngine import EventEngine
from Map import Map
from TreasureEvent import TreasureEventConfig
from market.GlobalMarket import IGlobalMarket


class GameEngine:

    def __init__(
            self,
            map: Map,
            event_engine: EventEngine,
            ticks_to_next_month: int,
            global_market: IGlobalMarket,
            tick_rate: float = None,
    ):
        self.tick_rate = tick_rate
        self.map = map
        self.event_engine = event_engine
        self.ticks_to_next_month = ticks_to_next_month
        self.event_engine.create_city_event(
            self.map.cities,
            TreasureEventConfig((200, 300))
        )
        self.tick = 1
        self.global_market = global_market

    def run(self):
        logger.info("Started GameEngine")
        while self.tick < 365:
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

        [city.show_price_history() for city in list(self.map.cities)]
        self.global_market.show_resource_units_count()
        plt.show(block=True)

    def _daily_update(self):
        for city in self.map.cities:
            city.update(self.tick)
        # self.event_engine.attempt_triggering_events()

    def _monthly_update(self):
        pass

    def _is_monthly_tick(self, tick: int):
        return tick % self.ticks_to_next_month == 0

    def _calculate_sleep_time_to_next_tick(self, time_at_beginning_of_tick: float, time_at_end_of_tick: float):
        return (time_at_beginning_of_tick + (1 / self.tick_rate)) - time_at_end_of_tick
