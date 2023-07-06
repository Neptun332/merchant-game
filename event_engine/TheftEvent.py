import random

from loguru import logger

from Probability import Probability
from city.ICity import ICity
from event_engine.Event import Event
from event_engine.IEventEngine import IEventEngine
from event_engine.config.BaseEventConfig import BaseEventConfig
from market.ResourceName import ResourceName


class TheftEvent(Event):
    MESSAGE: str = "In the City {city} thefs stole {units} units of {resource_name}"
    DEFAULT_PROBABILITY = Probability(0.01)

    def __init__(self, city: ICity, event_config: BaseEventConfig, event_engine: IEventEngine):
        self.city = city
        self.event_config = event_config
        self.event_engine = event_engine

        self.resource_units = None
        self.random_resource_name = None

    def handle(self):
        self.resource_units = random.randint(*self.event_config.units_count_range)
        self.random_resource_name = random.choice(list(ResourceName))
        self.city.local_market.remove_number_of_resources({self.random_resource_name: self.resource_units})
        self.event_engine.register_possible_event([TheftEvent(self.city, self.event_config, self.event_engine)])
        logger.info(self.get_message())

    def get_message(self) -> str:
        return self.MESSAGE.format(
            city=self.city.name,
            units=self.resource_units,
            resource_name=self.random_resource_name
        )

    def get_probability(self) -> Probability:
        return self.event_config.probability
