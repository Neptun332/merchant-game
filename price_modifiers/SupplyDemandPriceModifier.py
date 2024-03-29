from decimal import Decimal

import numpy

from Factor import Factor
from market.LocalMarket import LocalMarket
from market.ResourceName import ResourceName
from price_modifiers.IPriceModifier import IPriceModifier


class SupplyDemandPriceModifier(IPriceModifier):

    def __init__(self, demand_change_factor: Factor = Factor(Decimal("1"))):
        self.demand = 0
        self.supply = 0
        self.demand_change_factor = demand_change_factor

    def update(self,  context: LocalMarket, resource_name: ResourceName):
        self.demand = context.demand_per_resource.get(resource_name, 0)
        self.supply = context.get_resource_units(resource_name)

    def modify_price(self, base_price: Decimal) -> Decimal:
        demand_supply_price = self._calculate_demand_supply_price() * float(self.demand_change_factor.value)
        return base_price + Decimal(max(0, demand_supply_price))

    def _calculate_demand_supply_price(self) -> float:
        return numpy.log10(max(1, self.demand - self.supply))
