from decimal import Decimal
from typing import Dict

from market.Resource import Resource
from market.ResourceName import ResourceName


class CityUpgradeStrategy:

    def __init__(self, resources_needed: Dict[ResourceName, int]):
        self.resources_needed = resources_needed
        self.city_level = 1

        # Prosperity is reflection of economy strength. It should increase consumption of food.
        # If there is not enough food fo some time, prosperity should drop
        self.base_prosperity = 100
        self.prosperity = self._calculate_prosperity()

    def get_prosperity(self) -> int:
        return self.prosperity

    def get_demand_of_resources(self) -> Dict[ResourceName, int]:
        return self.resources_needed

    def can_upgrade(self, resources_map: Dict[ResourceName, Resource]) -> bool:
        return self._is_enough_all_resources(resources_map)

    def upgrade(self) -> Dict[ResourceName, int]:
        self.city_level += 1
        self.prosperity = self._calculate_prosperity()
        resource_cost = self.resources_needed
        self._increase_resource_needed()
        return resource_cost

    def get_city_level(self) -> int:
        return self.city_level

    def _increase_resource_needed(self):
        self.resources_needed = {resource_name: units * 2 for resource_name, units in self.resources_needed.items()}

    def _is_enough_all_resources(self, resources_map: Dict[ResourceName, Resource]) -> bool:
        return all([
            self._is_enough_resource(resources_map, resource_name)
            for resource_name in self.resources_needed.keys()
        ])

    def _is_enough_resource(self, resources_map: Dict[ResourceName, Resource], resource_name: ResourceName) -> bool:
        return resources_map[resource_name].get_units_count() >= self.resources_needed[
            resource_name] * Decimal('1.1')

    def _calculate_prosperity(self):
        return self.base_prosperity * self.city_level
