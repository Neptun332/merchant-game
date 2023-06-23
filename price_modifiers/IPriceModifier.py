from abc import ABC, abstractmethod
from decimal import Decimal

from market.ResourceName import ResourceName


class IPriceModifier(ABC):

    @abstractmethod
    def update(self, context: 'LocalMarket', resource_name: ResourceName):
        ...

    @abstractmethod
    def modify_price(self, base_price: Decimal) -> Decimal:
        ...
