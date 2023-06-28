from abc import ABC, abstractmethod
from typing import Optional, Tuple, Dict

from Factor import Factor
from market.Resource import Resource
from market.ResourceName import ResourceName


class IWorkshop(ABC):

    @abstractmethod
    def can_produce(self, resources_map: Dict[ResourceName, Resource]) -> bool:
        ...

    @abstractmethod
    def produce(self, production_boost: Factor) -> Tuple[Dict[ResourceName, int], Dict[ResourceName, int]]:
        ...


class Workshop(IWorkshop, ABC):

    def __init__(
            self,
            resource_name_produced: ResourceName,
            resource_units_produced: int,
            resource_name_consumed: Optional[ResourceName],  # Basic resources like wood stone does not consume anything
            resource_units_consumed: Optional[int],
            level: int
    ):
        self.resource_name_consumed = resource_name_consumed
        self.resource_units_consumed = resource_units_consumed
        self.resource_name_produced = resource_name_produced
        self.resource_units_produced = resource_units_produced
        self.level = level

    def upgrade(self):
        self.level += 1

    def get_produced_resource_name(self) -> ResourceName:
        return self.resource_name_produced
