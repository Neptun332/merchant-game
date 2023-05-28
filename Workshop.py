from abc import ABC, abstractmethod
from typing import Dict

from market.LocalMarket import LocalMarket
from market.ResourceName import ResourceName


class IWorkshop(ABC):

    @abstractmethod
    def can_produce(self) -> bool:
        ...

    @abstractmethod
    def produce(self):
        ...


class Workshop(IWorkshop):

    def __init__(
            self,
            resources_consumed: Dict[ResourceName, int],
            resources_produced: Dict[ResourceName, int],
            city_level: int,
            local_market: LocalMarket
    ):
        self.resources_consumed = resources_consumed
        self.resources_produced = resources_produced
        self.city_level = city_level
        self.local_market = local_market

    def upgrade(self, city_level: int):
        self.city_level = city_level

    def can_produce(self) -> bool:
        return all([
            self.local_market.resources_map.get(resource_name, 0) > units
            for resource_name, units in self.resources_consumed.items()
        ])

    def produce(self):
        self.local_market.remove_resources(self.resources_consumed)
        self.local_market.add_resources(self.resources_produced)
