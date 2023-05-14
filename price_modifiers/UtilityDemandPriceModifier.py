from decimal import Decimal

import numpy

from Factor import Factor
from price_modifiers.IPriceModifier import IPriceModifier


class UtilityDemandPriceModifier(IPriceModifier):

    def __init__(self, demand_change_factor: Factor = Factor(Decimal("1"))):
        self.demand = 0
        self.utility = 0
        self.demand_change_factor = demand_change_factor

    def update(self, demand: int, utility: int):
        self.demand = demand
        self.utility = utility

    def modify_price(self, base_price: Decimal) -> Decimal:
        demand_utility_price = self._calculate_demand_utility_price() * float(self.demand_change_factor.value)
        return base_price + Decimal(max(0, demand_utility_price))

    def _calculate_demand_utility_price(self) -> float:
        return numpy.log10(max(1, self.demand - self.utility))
