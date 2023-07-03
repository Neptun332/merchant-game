from typing import Tuple, Dict, List

from Factor import Factor
from city.ICity import ICity
from market.Resource import Resource
from market.ResourceName import ResourceName
from market.Unit import Unit
from workshop.Workshop import Workshop


class NotConsumingWorkshop(Workshop):

    def __init__(
            self,
            resource_name_produced: ResourceName,
            resource_units_produced: int,
            level: int,
            produced_unit_ticks_lifetime: int = Unit.DEFAULT_UNIT_LIFE_TIME
    ):
        super().__init__(
            resource_name_produced=resource_name_produced,
            resource_units_produced=resource_units_produced,
            resource_name_consumed=None,
            resource_units_consumed=None,
            level=level,
            produced_unit_ticks_lifetime=produced_unit_ticks_lifetime
        )

    def can_produce(self, resources_map: Dict[ResourceName, Resource]) -> bool:
        return True

    def produce(
            self,
            production_boost: Factor,
            producer_city: ICity,
            current_tick: int
    ) -> Tuple[Dict[ResourceName, int], Dict[ResourceName, List[Unit]]]:
        return {}, {
            self.resource_name_produced: self._create_number_of_units(
                number_of_units=self._calculate_number_of_units(production_boost),
                producer_city=producer_city,
                unit_ttl=self._calculate_unit_ttl(current_tick),
            )
        }
