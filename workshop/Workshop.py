from abc import ABC, abstractmethod
from typing import Optional, Tuple, Dict, List

from Factor import Factor
from city.ICity import ICity
from market.Resource import Resource
from market.ResourceName import ResourceName
from market.Unit import Unit


class IWorkshop(ABC):

    @abstractmethod
    def can_produce(self, resources_map: Dict[ResourceName, Resource]) -> bool:
        ...

    @abstractmethod
    def produce(
            self,
            production_boost: Factor,
            producer_city: ICity,
            current_tick: int
    ) -> Tuple[Dict[ResourceName, int], Dict[ResourceName, List[Unit]]]:        ...


class Workshop(IWorkshop, ABC):

    def __init__(
            self,
            resource_name_produced: ResourceName,
            resource_units_produced: int,
            resource_name_consumed: Optional[ResourceName],  # Basic resources like wood stone does not consume anything
            resource_units_consumed: Optional[int],
            level: int,
            produced_unit_ticks_lifetime: int = Unit.DEFAULT_UNIT_LIFE_TIME
    ):
        self.resource_name_consumed = resource_name_consumed
        self.resource_units_consumed = resource_units_consumed
        self.resource_name_produced = resource_name_produced
        self.resource_units_produced = resource_units_produced
        self.level = level
        self.produced_unit_ticks_lifetime = produced_unit_ticks_lifetime

    def upgrade(self):
        self.level += 1

    def get_produced_resource_name(self) -> ResourceName:
        return self.resource_name_produced

    def _calculate_number_of_units(self, production_boost: Factor) -> int:
        return int(self.resource_units_produced * self.level * production_boost.value)

    def _create_number_of_units(self, number_of_units: int, producer_city: ICity, unit_ttl: int) -> List[Unit]:
        return [self._create_unit(producer_city, unit_ttl) for _ in range(number_of_units)]

    def _create_unit(self, city: ICity, unit_ttl: int) -> Unit:
        return Unit(
            ttl=unit_ttl,
            produced_by=city
        )

    def _calculate_unit_ttl(self, current_tick: int) -> int:
        return current_tick + self.produced_unit_ticks_lifetime
