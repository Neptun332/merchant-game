from decimal import Decimal

from market.ResourceName import ResourceName
from price_modifiers.IPriceModifier import IPriceModifier


class NoOpPriceModifier(IPriceModifier):

    def update(self, context: 'LocalMarket', resource_name: ResourceName):
        pass

    def modify_price(self, base_price: Decimal) -> Decimal:
        return base_price
