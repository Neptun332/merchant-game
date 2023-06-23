from abc import ABC, abstractmethod

from market.LocalMarket import LocalMarket
from market.ResourceName import ResourceName


class IGlobalMarket(ABC):

    @abstractmethod
    def set_local_market(self, local_market: LocalMarket):
        ...

    @abstractmethod
    def get_all_gold(self) -> int:
        ...


class GlobalMarket(IGlobalMarket):

    def __init__(self):
        self.local_markets = {}

    def set_local_market(self, local_market: LocalMarket):
        self.local_markets[id(local_market)] = local_market

    def get_all_gold(self):
        return sum([local_market.resources_map[ResourceName.Gold].units for local_market in self.local_markets.values()])
