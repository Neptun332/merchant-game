import random

from loguru import logger

from City import City
from Event import Event, EventStateEnum
from Percentage import Percentage
from config.TreasureEventConfig import TreasureEventConfig


class TreasureEvent(Event):
    MESSAGE: str = "In the City {} found chest with gold. To the treasury was added {}"
    PROBABILITY_EACH_TICK: Percentage = 0.001

    def __init__(self, city: City, event_config: TreasureEventConfig):
        self.city = city
        self.gold_value = random.randint(*event_config.gold_range)

    def handle(self):
        self.city.add_gold(self.gold_value)
        self.state = EventStateEnum.TRIGGERED
        logger.info(self.get_message())

    def get_message(self) -> str:
        return self.MESSAGE.format(self.city.name, self.gold_value)

    def calculate_probability(self):
        return self.PROBABILITY_EACH_TICK
