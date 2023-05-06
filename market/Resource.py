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
    demand_change_factor: Factor
    price_per_unit: Decimal = None
    history_of_price: List = field(default_factory=list)

    def add_units(self, units: int):
        self.units += units

    def remove_units(self, units: int):
        self.units -= units

    def update(self, demand: int) -> Decimal:
        clipped_demand = numpy.clip(demand, 0, self.units)
        self.price_per_unit = Decimal((self.units - clipped_demand) / self.demand_change_factor.value)
        self.history_of_price.append(self.price_per_unit)
        return self.price_per_unit
