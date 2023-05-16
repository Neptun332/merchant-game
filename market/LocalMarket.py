import math
from typing import Dict

import matplotlib.pyplot as plt
import pandas as pd

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

        self.utility_demand_price_modifiers: Dict[ResourceName, IPriceModifier] = {}
        self.default_price_modifier = NoOpPriceModifier()

    def update(self, demand: Dict[ResourceName, int]):
        for resource_name, resource in self.resources_map.items():
            price_modifier = self.utility_demand_price_modifiers.get(resource_name, self.default_price_modifier)
            price_modifier.update(demand.get(resource_name, 0), self.get_resource_units(resource_name))
            resource.update_price()

    def remove_resources(self, resource_units: Dict[ResourceName, int]):
        [resource.remove_units(resource_units.get(resource_name, 0)) for resource_name, resource in
         self.resources_map.items()]

    def get_resource_units(self, resource_name: ResourceName):
        if resource_name in self.resources_map.keys():
            return self.resources_map[resource_name].units
        return 0

    def add_utility_demand_modifier(self, price_modifier: IPriceModifier, resource_name: ResourceName):
        self.utility_demand_price_modifiers[resource_name] = price_modifier
        resource = self.resources_map.get(resource_name, None)
        if resource:
            resource.add_price_modifier(price_modifier)

    def remove_utility_demand_modifier(self, resource_name: ResourceName):
        price_modifier = self.utility_demand_price_modifiers.pop(resource_name, None)
        resource = self.resources_map.get(resource_name, None)
        if resource and price_modifier:
            resource.remove_price_modifier(price_modifier)

    def show_price_history(self):
        subplot_size = math.ceil(len(self.resources_map.keys()) / 2)
        fig, axes = plt.subplots(nrows=subplot_size, ncols=subplot_size)
        fig.tight_layout(pad=3)
        fig.set_size_inches(15, 10)
        for index, (resource_name, resource) in enumerate(self.resources_map.items()):
            data = pd.DataFrame(resource.history_of_price).apply(pd.to_numeric, downcast='float')

            subplot_column = index % subplot_size
            subplot_row = int(index / subplot_size)
            data.plot(figsize=(20, 20), title='Resources price', subplots=True, ax=axes[subplot_row, subplot_column])
            axes[subplot_row, subplot_column].title.set_text(resource_name)

        plt.show(block=True)
