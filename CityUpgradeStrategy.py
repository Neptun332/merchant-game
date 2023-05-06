from decimal import Decimal
from typing import Dict

from market.Resource import Resource
from market.ResourceName import ResourceName


class CityUpgradeStrategy:

    def __init__(self, resources_needed: Dict[ResourceName, int]):
        self.resources_needed = resources_needed
        self.city_level = 1

    def get_demand_of_resources(self, resources_map: Dict[ResourceName, Resource]) -> Dict[ResourceName, int]:
        return {
            resource_name: needed_units - resources_map.get(resource_name, 0).units
            for resource_name, needed_units in self.resources_needed.items()
        }

    def can_upgrade(self, resources_map: Dict[ResourceName, Resource]) -> bool:
        return all([
            self._is_enough_resource(resources_map, resource_name)
            for resource_name in self.resources_needed.keys()
        ])

    def upgrade(self, resources_map: Dict[ResourceName, Resource]):
        if self.can_upgrade(resources_map):
            resources_map = self._modify_resource_units(resources_map)
            self.city_level += 1

        return resources_map

    def _modify_resource_units(self, resources_map: Dict[ResourceName, Resource]) -> Dict[ResourceName, Resource]:
        for resource_name, value_needed in self.resources_needed.items():
            resources_map[resource_name].remove_units(value_needed)
        return resources_map

    def _is_enough_resource(self, resources_map: Dict[ResourceName, Resource], resource_name: ResourceName):
        return resources_map.get(resource_name, 0).units * Decimal('1.1') >= self.resources_needed[
            resource_name] * self.city_level
