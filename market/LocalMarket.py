from typing import Dict

from market.Resource import Resource
from market.ResourceName import ResourceName


class LocalMarket:

    def __init__(self, resources_map: Dict[ResourceName, Resource]):
        self.resources_map = resources_map

    def update(self, demand: Dict[ResourceName, int]):
        for resource_name, resource in self.resources_map.items():
            resource.update(demand.get(resource_name, 0))

    def remove_resources(self, resource_units: Dict[ResourceName, int]):
        [resource.remove_units(resource_units.get(resource_name, 0)) for resource_name, resource in
         self.resources_map.items()]
