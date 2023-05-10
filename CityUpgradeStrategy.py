from decimal import Decimal
from typing import Dict

from market.Resource import Resource
from market.ResourceName import ResourceName


class CityUpgradeStrategy:

    def __init__(self, resources_needed: Dict[ResourceName, int]):
        self.resources_needed = resources_needed
        self.city_level = 1

    def get_demand_of_resources(self) -> Dict[ResourceName, int]:
        return self.resources_needed

    def can_upgrade(self, resources_map: Dict[ResourceName, Resource]) -> bool:
        return all([
            self._is_enough_resource(resources_map, resource_name)
            for resource_name in self.resources_needed.keys()
        ])

    def upgrade(self) -> Dict[ResourceName, int]:
        self.city_level += 1
        resource_cost = self.resources_needed
        self._increase_resource_needed()
        return resource_cost

    def _increase_resource_needed(self):
        self.resources_needed = {resource_name: units * 2 for resource_name, units in self.resources_needed.items()}

    def _is_enough_resource(self, resources_map: Dict[ResourceName, Resource], resource_name: ResourceName):
        return resources_map.get(resource_name, 0).units >= self.resources_needed[
            resource_name] * Decimal('1.1')
