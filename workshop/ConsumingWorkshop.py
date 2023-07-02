from typing import Tuple, Dict, List

from Factor import Factor
from city.City import City
from market.Resource import Resource
from market.ResourceName import ResourceName
from market.Unit import Unit
from workshop.Workshop import Workshop


class ConsumingWorkshop(Workshop):

    def can_produce(self, resources_map: Dict[ResourceName, Resource]) -> bool:
        return resources_map[self.resource_name_consumed].get_units_count() > self.resource_units_consumed

    def produce(
            self,
            production_boost: Factor,
            producer_city: City,
            current_tick: int
    ) -> Tuple[Dict[ResourceName, int], Dict[ResourceName, List[Unit]]]:
        return {self.resource_name_consumed: self.resource_units_consumed * self.level}, \
            {
                self.resource_name_produced: self._create_number_of_units(
                    number_of_units=self._calculate_number_of_units(production_boost),
                    producer_city=producer_city,
                    current_tick=current_tick,
                )
            }
