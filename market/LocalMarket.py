from collections import defaultdict
from typing import Dict

from market.Resource import Resource
from market.ResourceName import ResourceName
from price_modifiers.IPriceModifier import IPriceModifier
from price_modifiers.NoOpPriceModifier import NoOpPriceModifier


class LocalMarket:

    def __init__(
            self,
            resources_map: Dict[ResourceName, Resource],
    ):
        self.resources_map = resources_map
        # TODO make price_modifiers a class that holds info about price modifiers per resource so you can update them with dedicated methods
        self.price_modifiers = defaultdict(list)
        self.default_price_modifier = NoOpPriceModifier()

    def update(self, demand: Dict[ResourceName, int]):
        for resource_name, resource in self.resources_map.items():
            price_modifiers = self.price_modifiers.get(resource_name, [self.default_price_modifier])
            [
                modifier.update(demand.get(resource_name, 0), self.get_resource_units(resource_name))
                for modifier in price_modifiers
            ]
            resource.update_price()

    def remove_resources(self, resource_units: Dict[ResourceName, int]):
        [resource.remove_units(resource_units.get(resource_name, 0)) for resource_name, resource in
         self.resources_map.items()]

    def get_resource_units(self, resource_name: ResourceName):
        if resource_name in self.resources_map.keys():
            return self.resources_map[resource_name].units
        return 0

    def add_price_modifier(self, price_modifier: IPriceModifier, resource_name: ResourceName):
        self.price_modifiers[resource_name].append(price_modifier)
        # TODO temporary
        resource = self.resources_map.get(resource_name, None)
        if resource:
            resource.add_price_modifier(price_modifier)

    def remove_price_modifier(self, price_modifier: IPriceModifier, resource_name: ResourceName):
        self.price_modifiers[resource_name].remove(price_modifier)
        # TODO temporary
        resource = self.resources_map.get(resource_name, None)
        if resource:
            resource.remove_price_modifier(price_modifier)
