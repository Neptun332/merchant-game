from typing import Dict

import numpy

from market.Resource import Resource
from market.ResourceName import ResourceName


class LocalMarket:

    def __init__(self, resources_map: Dict[ResourceName, Resource]):
        self.resources_map = resources_map

    def update(self, demand: Dict[ResourceName, int]):
        utility = self._get_utility_v2()
        for resource_name, resource in self.resources_map.items():
            resource.update(demand.get(resource_name, 0), utility.get(resource_name, 0))

    def remove_resources(self, resource_units: Dict[ResourceName, int]):
        [resource.remove_units(resource_units.get(resource_name, 0)) for resource_name, resource in
         self.resources_map.items()]

    def _get_utility(self, demand: Dict[ResourceName, int]) -> Dict[ResourceName, int]:
        return {
            resource_name: 12*numpy.log2(max(0, float(self.resources_map.get(resource_name, 0).units) +2))
            for resource_name, units in demand.items()
        }

    def _get_utility_v2(self) -> Dict[ResourceName, int]:
        return {
            resource_name: resource.units
            for resource_name, resource in self.resources_map.items()
        }




# Utility is something you cna count, lets calculate demand based on missing resources (magic way)