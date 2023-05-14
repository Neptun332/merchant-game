from abc import ABC, abstractmethod
from decimal import Decimal


class IPriceModifier(ABC):

    def update(self, demand: int, utility: int):
        ...

    @abstractmethod
    def modify_price(self, base_price: Decimal) -> Decimal:
        ...
