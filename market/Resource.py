from dataclasses import dataclass, field
from decimal import Decimal
from typing import List

import numpy

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

    def update(self, demand: int, utility: int, demand_change_factor: Factor = Factor(Decimal("1"))) -> Decimal:
        price_per_unit = self._price_per_unit_based_on_demand(demand, utility) * float(demand_change_factor.value)
        self.price_per_unit = Decimal(max(0, price_per_unit))
        self.history_of_price.append(self.price_per_unit)
        return self.price_per_unit

    def _price_per_unit_based_on_demand(self, demand: int, utility: int, ) -> float:
        return 1 * numpy.log2(max(0, float(demand - utility) - 100))
