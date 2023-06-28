from typing import Tuple, Dict

from Factor import Factor
from market.Resource import Resource
from market.ResourceName import ResourceName
from workshop.Workshop import Workshop


class ConsumingWorkshop(Workshop):

    def can_produce(self, resources_map: Dict[ResourceName, Resource]) -> bool:
        return resources_map.get(self.resource_name_consumed, 0).units > self.resource_units_consumed

    def produce(self, production_boost: Factor) -> Tuple[Dict[ResourceName, int], Dict[ResourceName, int]]:
        return {self.resource_name_consumed: self.resource_units_consumed * self.level}, \
            {
                self.resource_name_produced:
                    int(self.resource_units_produced * self.level * production_boost.value)
            }
