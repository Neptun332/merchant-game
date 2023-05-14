from dataclasses import dataclass, field
from decimal import Decimal
from typing import List

from price_modifiers.IPriceModifier import IPriceModifier
from market.ResourceName import ResourceName


@dataclass
class Resource:
    name: ResourceName
    units: int
    base_price: Decimal  # Costs of production and materials
    price_per_unit: Decimal = None
    history_of_price: List = field(default_factory=list)
    price_modifiers: List = field(default_factory=list)

    def add_units(self, units: int):
        self.units += units

    def remove_units(self, units: int):
        self.units -= units

    def add_price_modifier(self, price_modifier: IPriceModifier):
        self.price_modifiers.append(price_modifier)

    def remove_price_modifier(self, price_modifier: IPriceModifier):
        self.price_modifiers.remove(price_modifier)

    def update_price(self):
        for price_modifier in self.price_modifiers:
            self.price_per_unit = price_modifier.modify_price(self.base_price)
            self.history_of_price.append(self.price_per_unit)


