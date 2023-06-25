from abc import ABC, abstractmethod
from decimal import Decimal
from typing import Dict

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

        self._validate()

    def _validate(self):
        if sum([unit_price_factor.value for unit_price_factor in self.unit_price_factor_per_resource.values()]) > 1:
            raise ValueError("Sum of all unit_price_factor should not be greater than 1")

    def set_local_markets(self, local_markets: Dict[int, LocalMarket]):
        self.local_markets = local_markets
        self.update()

    def update(self):
        all_gold = self.get_resource_unit_count(ResourceName.Gold)
        for resource_name in ResourceName:
            if resource_name is ResourceName.Gold:
                continue
            for local_market in self.local_markets.values():
                resource_unit_price_factor = self.unit_price_factor_per_resource[resource_name]
                if not (resource_unit_count := self.get_resource_unit_count(resource_name)):
                    continue
                new_base_price = Decimal((all_gold * resource_unit_price_factor.value) / resource_unit_count)
                local_market.set_resource_base_price(new_base_price, resource_name)

    def get_resource_unit_count(self, resource_name: ResourceName) -> int:
        return sum([local_market.get_resource_units(resource_name) for local_market in self.local_markets.values()])
