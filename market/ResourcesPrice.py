from dataclasses import dataclass
from decimal import Decimal

from Percentage import Percentage


@dataclass
class ResourcesPrice:
    wheat: Decimal
    wood: Decimal
    stone: Decimal

    def increase_price_of_all_by_percentage(self, percentage: Percentage):
        self.wheat *= 1 + percentage.value
        self.wood *= 1 + percentage.value
        self.stone *= 1 + percentage.value
