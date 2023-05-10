from dataclasses import dataclass, field
from decimal import Decimal
from typing import List

from Factor import Factor
from market.ResourceName import ResourceName


@dataclass
class Resource:
    name: ResourceName
    units: int
    price_per_unit: Decimal = None
    history_of_price: List = field(default_factory=list)

    def add_units(self, units: int):
        self.units += units

    def remove_units(self, units: int):
        self.units -= units

    def update(self, demand: int, demand_change_factor: Factor = Factor(Decimal("0.5"))) -> Decimal:
        self.price_per_unit = Decimal(max(0, demand * demand_change_factor.value))
        self.history_of_price.append(self.price_per_unit)
        return self.price_per_unit
