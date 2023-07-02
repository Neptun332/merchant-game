import math
from decimal import Decimal
from typing import Dict, List

import matplotlib.pyplot as plt
import pandas as pd

from market.Resource import Resource
from market.ResourceName import ResourceName
from market.Unit import Unit
from price_modifiers.IPriceModifier import IPriceModifier
from price_modifiers.NoOpPriceModifier import NoOpPriceModifier


class LocalMarket:

    def __init__(
            self,
            resources_map: Dict[ResourceName, Resource],
    ):
        self.resources_map = resources_map

        self.supply_demand_price_modifiers: Dict[ResourceName, IPriceModifier] = {}
        self.default_price_modifier = NoOpPriceModifier()
        self.demand_per_resource = {}

    def update(self, demand: Dict[ResourceName, int], current_tick: int):
        self.demand_per_resource = demand
        for resource_name, resource in self.resources_map.items():
            price_modifier = self.supply_demand_price_modifiers.get(resource_name, self.default_price_modifier)
            price_modifier.update(self, resource_name)
            resource.update_price()
            resource.remove_expired_units(current_tick)

    def remove_number_of_resources(self, resource_units: Dict[ResourceName, int]):
        [self.resources_map[resource_name].remove_number_of_units(units) for resource_name, units in
         resource_units.items()]

    def add_resources(self, resource_units: Dict[ResourceName, List[Unit]]):
        [self.resources_map[resource_name].add_units(units) for resource_name, units in
         resource_units.items()]

    def get_resource_units(self, resource_name: ResourceName):
        if resource_name in self.resources_map.keys():
            return self.resources_map[resource_name].get_units_count()
        return 0

    def add_supply_demand_modifier(self, price_modifier: IPriceModifier, resource_name: ResourceName):
        self.supply_demand_price_modifiers[resource_name] = price_modifier
        resource = self.resources_map.get(resource_name, None)
        if resource:
            resource.add_price_modifier(price_modifier)

    def remove_supply_demand_modifier(self, resource_name: ResourceName):
        price_modifier = self.supply_demand_price_modifiers.pop(resource_name, None)
        resource = self.resources_map.get(resource_name, None)
        if resource and price_modifier:
            resource.remove_price_modifier(price_modifier)

    def show_price_history(self, city_name: str):
        subplot_size = math.ceil(math.sqrt(len(self.resources_map.keys())))
        fig, axes = plt.subplots(nrows=subplot_size, ncols=subplot_size)
        fig.tight_layout(pad=3)
        fig.set_size_inches(15, 10)
        for index, (resource_name, resource) in enumerate(self.resources_map.items()):
            data = pd.DataFrame(resource.history_of_price).apply(pd.to_numeric, downcast='float')

            subplot_column = index % subplot_size
            subplot_row = int(index / subplot_size)
            data.plot(figsize=(20, 20), title=f'Resources price, city_name={city_name}', subplots=True,
                      ax=axes[subplot_row, subplot_column])
            axes[subplot_row, subplot_column].title.set_text(resource_name)

        plt.show(block=False)

    def set_resource_base_price(self, base_price: Decimal, resource_name: ResourceName):
        if resource := self.resources_map.get(resource_name):
            resource.base_price = base_price

    def set_produced_by_on_resource_units(self, produced_by: 'City'):
        [[unit.set_produced_by(produced_by) for unit in resource.units] for _, resource in self.resources_map.items()]
