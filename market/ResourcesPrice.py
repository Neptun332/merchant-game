from dataclasses import dataclass
from decimal import Decimal

from Factor import Factor


@dataclass
class ResourcesPrice:
    wheat: Decimal
    wood: Decimal
    stone: Decimal

    def increase_price_of_all_by_factor(self, factor: Factor):
        self.wheat *= 1 + factor.value
        self.wood *= 1 + factor.value
        self.stone *= 1 + factor.value
