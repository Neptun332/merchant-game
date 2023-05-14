from decimal import Decimal

from price_modifiers.IPriceModifier import IPriceModifier


class NoOpPriceModifier(IPriceModifier):

    def modify_price(self, base_price: Decimal) -> Decimal:
        return base_price
