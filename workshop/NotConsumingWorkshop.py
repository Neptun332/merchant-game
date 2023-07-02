from typing import Tuple, Dict, List

from Factor import Factor
from city.City import City
from market.Resource import Resource
from market.ResourceName import ResourceName
from market.Unit import Unit
from workshop.Workshop import Workshop


class NotConsumingWorkshop(Workshop):

    def __init__(
            self,
            resource_name_produced: ResourceName,
            resource_units_produced: int,
            level: int
    ):
        super().__init__(
            resource_name_produced=resource_name_produced,
            resource_units_produced=resource_units_produced,
            resource_name_consumed=None,
            resource_units_consumed=None,
            level=level)

    def can_produce(self, resources_map: Dict[ResourceName, Resource]) -> bool:
        return True

    def produce(
            self,
            production_boost: Factor,
            producer_city: City,
            current_tick: int
    ) -> Tuple[Dict[ResourceName, int], Dict[ResourceName, List[Unit]]]:
        return {}, {
            self.resource_name_produced: self._create_number_of_units(
                number_of_units=self._calculate_number_of_units(production_boost),
                producer_city=producer_city,
                current_tick=current_tick,
            )
        }


