from abc import ABC, abstractmethod

from market.LocalMarket import LocalMarket
from market.ResourceName import ResourceName


class IGlobalMarket(ABC):

    @abstractmethod
    def set_local_market(self, local_market: LocalMarket):
        ...

    @abstractmethod
    def get_resource_unit_count(self, resource_name: ResourceName) -> int:
        ...


class GlobalMarket(IGlobalMarket):

    def __init__(self):
        self.local_markets = {}

    def set_local_market(self, local_market: LocalMarket):
        self.local_markets[id(local_market)] = local_market

    def update(self):
        units_per_resource = {}
        for resource_name in ResourceName:
            if resource_name is ResourceName.Gold:
                continue
            units_per_resource[resource_name] = self.get_resource_unit_count(resource_name)

        sum_of_all_units = sum(units_per_resource.values())
        all_gold = self.get_resource_unit_count(ResourceName.Gold)
        for resource_name in ResourceName:
            for local_market in self.local_markets.values():
                resource_market_representation = units_per_resource[resource_name] / sum_of_all_units
                new_base_price = (all_gold * resource_market_representation) / sum_of_all_units
                local_market.set_resource_base_price(new_base_price, resource_name)

    def get_resource_unit_count(self, resource_name: ResourceName) -> int:
        return sum([local_market.get_resource_units(resource_name) for local_market in self.local_markets.values()])
