from typing import Tuple, Dict

from Factor import Factor
from market.Resource import Resource
from market.ResourceName import ResourceName
from workshop.Workshop import Workshop


class NotConsumingWorkshop(Workshop):

    def __init__(
            self,
            resource_name_produced: ResourceName,
            resource_units_produced: int,
            city_level: int
    ):
        super().__init__(
            resource_name_produced=resource_name_produced,
            resource_units_produced=resource_units_produced,
            resource_name_consumed=None,
            resource_units_consumed=None,
            city_level=city_level)

    def can_produce(self, resources_map: Dict[ResourceName, Resource]) -> bool:
        return True

    def produce(self, production_boost: Factor) -> Tuple[Dict[ResourceName, int], Dict[ResourceName, int]]:
        return {}, {
            self.resource_name_produced:
                int(self.resource_units_produced * self.city_level * production_boost.value)
        }
