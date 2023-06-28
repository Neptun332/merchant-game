import math
from abc import ABC, abstractmethod
from collections import defaultdict
from decimal import Decimal
from typing import Dict, List

import pandas as pd
from matplotlib import pyplot as plt

from Factor import Factor
from market.LocalMarket import LocalMarket
from market.ResourceName import ResourceName


class IGlobalMarket(ABC):

    @abstractmethod
    def set_local_markets(self, local_markets: Dict[int, LocalMarket]):
        ...

    @abstractmethod
    def get_resource_unit_count(self, resource_name: ResourceName) -> int:
        ...

    @abstractmethod
    def update(self):
        ...


class GlobalMarket(IGlobalMarket):

    def __init__(self, unit_price_factor_per_resource: Dict[ResourceName, Factor]):
        self.unit_price_factor_per_resource = unit_price_factor_per_resource
        self.local_markets = {}
        self.resource_units_history: Dict[ResourceName, List[int]] = defaultdict(list)

        self._validate()

    def _validate(self):
        if sum([unit_price_factor.value for unit_price_factor in self.unit_price_factor_per_resource.values()]) > 1:
            raise ValueError("Sum of all unit_price_factor should not be greater than 1")

    def set_local_markets(self, local_markets: Dict[int, LocalMarket]):
        self.local_markets = local_markets
        self.update()

    def update(self):
        all_gold = self.get_resource_unit_count(ResourceName.Gold)
        self.resource_units_history[ResourceName.Gold].append(all_gold)
        for resource_name in ResourceName:
            if resource_name is ResourceName.Gold:
                continue
            for local_market in self.local_markets.values():
                resource_unit_price_factor = self.unit_price_factor_per_resource[resource_name]
                resource_unit_count = self.get_resource_unit_count(resource_name)
                self.resource_units_history[resource_name].append(resource_unit_count)
                if not (resource_unit_count):
                    continue
                new_base_price = Decimal((all_gold * resource_unit_price_factor.value) / resource_unit_count)
                local_market.set_resource_base_price(new_base_price, resource_name)

    def get_resource_unit_count(self, resource_name: ResourceName) -> int:
        return sum([local_market.get_resource_units(resource_name) for local_market in self.local_markets.values()])

    def show_resource_units_count(self):
        subplot_size = math.ceil(math.sqrt(len(self.resource_units_history.keys())))
        fig, axes = plt.subplots(nrows=subplot_size, ncols=subplot_size)
        fig.tight_layout(pad=3)
        fig.set_size_inches(15, 10)
        for index, (resource_name, units_history) in enumerate(self.resource_units_history.items()):
            data = pd.DataFrame(units_history)

            subplot_column = index % subplot_size
            subplot_row = int(index / subplot_size)
            data.plot(figsize=(20, 20), title=f'All resource units in whole market', subplots=True, ax=axes[subplot_row, subplot_column])
            axes[subplot_row, subplot_column].title.set_text(resource_name)

        plt.show(block=False)