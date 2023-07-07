import random
from decimal import Decimal

from loguru import logger

from Factor import Factor
from Probability import Probability
from city.ICity import ICity
from event_engine.Event import Event
from event_engine.IEventEngine import IEventEngine
from event_engine.config.BaseEventConfig import BaseEventConfig
from market.ResourceName import ResourceName


class TheftEvent(Event):
    MESSAGE: str = "In the City {city} thefs stole {units} units of {resource_name}"
    DEFAULT_PROBABILITY = Probability(0.1)
    DEFAULT_MODIFIER_PER_RESOURCE = {
        ResourceName.Gold: Factor(Decimal(10))
    }

    def __init__(self, city: ICity, event_config: BaseEventConfig, event_engine: IEventEngine):
        self.city = city
        self.event_config = event_config
        self.event_engine = event_engine

        self.resource_units = None
        self.random_resource_name = None

    def handle(self):
        self.random_resource_name = random.choice(list(ResourceName))
        self.resource_units = self._calculate_units_count()
        self.city.local_market.remove_number_of_resources({self.random_resource_name: self.resource_units})
        self._re_register_event()
        logger.info(self.get_message())

    def get_message(self) -> str:
        return self.MESSAGE.format(
            city=self.city.name,
            units=self.resource_units,
            resource_name=self.random_resource_name
        )

    def get_probability(self) -> Probability:
        return self.event_config.probability

    def _re_register_event(self):
        self.event_engine.register_possible_event([TheftEvent(self.city, self.event_config, self.event_engine)])

    def _calculate_units_count(self) -> int:
        units_modifier = self.DEFAULT_MODIFIER_PER_RESOURCE.get(self.random_resource_name, Factor.from_default()).value
        return int(random.randint(*self.event_config.units_count_range) * units_modifier)
