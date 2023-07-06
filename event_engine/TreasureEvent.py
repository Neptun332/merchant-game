import random

from loguru import logger

from event_engine.Event import Event, EventStateEnum
from Probability import Probability
from city.ICity import ICity
from event_engine.config.BaseEventConfig import BaseEventConfig


class TreasureEvent(Event):
    MESSAGE: str = "In the City {} found chest with gold. To the treasury was added {}"
    PROBABILITY_EACH_TICK: Probability = 0.001

    def __init__(self, city: ICity, event_config: BaseEventConfig):
        self.city = city
        self.gold_value = random.randint(*event_config.units_count_range)

    def handle(self):
        self.city.add_gold(self.gold_value)
        self.state = EventStateEnum.TRIGGERED
        logger.info(self.get_message())

    def get_message(self) -> str:
        return self.MESSAGE.format(self.city.name, self.gold_value)

    def calculate_probability(self):
        return self.PROBABILITY_EACH_TICK
