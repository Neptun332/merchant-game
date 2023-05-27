from abc import ABC, abstractmethod
from typing import Dict, Tuple

from market.LocalMarket import LocalMarket
from market.Resource import Resource
from market.ResourceName import ResourceName


class IWorkshop(ABC):

    @abstractmethod
    def can_produce(self, resources_map: Dict[ResourceName, Resource]) -> bool:
        ...

    @abstractmethod
    def consume(self, resources_map: Dict[ResourceName, Resource]):
        ...

    @abstractmethod
    def produce(self) -> Tuple[ResourceName, int]:
        ...


class Workshop(IWorkshop):

    def __init__(
            self,
            resources_consumed: Dict[ResourceName, int],
            resources_produced: Tuple[ResourceName, int],
            city_level: int
    ):
        self.resources_consumed = resources_consumed
        self.resources_produced = resources_produced
        self.city_level = city_level

    def upgrade(self, city_level: int):
        self.city_level = city_level

    def can_produce(self, local_market: LocalMarket) -> bool:
        return all([
            local_market.resources_map.get(resource_name, 0) > units
            for resource_name, units in self.resources_consumed.items()
        ])

    def consume(self, local_market: LocalMarket):
        resources_map.

    def produce(self) -> Tuple[ResourceName, int]:
        pass
