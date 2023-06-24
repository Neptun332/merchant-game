from decimal import Decimal

from market.GlobalMarket import GlobalMarket
from market.LocalMarket import LocalMarket
from market.ResourceName import ResourceName
from price_modifiers.IPriceModifier import IPriceModifier


class UnitsBasedPriceModifier(IPriceModifier):

    def __init__(self, global_market: GlobalMarket):
        self.global_market = global_market

    def update(self, context: LocalMarket, resource_name: ResourceName):
        units_per_resource = {}
        for resource_name in ResourceName:
            if resource_name is ResourceName.Gold:
                continue
            units_per_resource[resource_name] = self.global_market.get_resource_unit_count(resource_name)

        sum_of_all_units = sum(units_per_resource.values())
        all_gold = self.global_market.get_resource_unit_count(ResourceName.Gold)

    def modify_price(self, base_price: Decimal) -> Decimal:
        pass
