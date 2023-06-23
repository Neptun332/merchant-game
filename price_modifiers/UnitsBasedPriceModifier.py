from decimal import Decimal

from market.GlobalMarket import GlobalMarket
from market.LocalMarket import LocalMarket
from market.ResourceName import ResourceName
from price_modifiers.IPriceModifier import IPriceModifier


class UnitsBasedPriceModifier(IPriceModifier):

    def __init__(self, global_market: GlobalMarket):
        self.global_market = global_market

    def update(self, context: LocalMarket, resource_name: ResourceName):
        pass

    def modify_price(self, base_price: Decimal) -> Decimal:
        pass
