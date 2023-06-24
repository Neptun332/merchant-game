from dataclasses import dataclass, field
from decimal import Decimal
from typing import List

from market.ResourceName import ResourceName
from price_modifiers.IPriceModifier import IPriceModifier


@dataclass
class Resource:
    name: ResourceName
    units: int
    base_price: Decimal  # Costs of production and materials
    price_per_unit: Decimal = None
    history_of_price: List = field(default_factory=lambda: [])
    price_modifiers: List = field(default_factory=list)

    def __post_init__(self):
        self.price_per_unit = self.base_price
        self.history_of_price = [self.price_per_unit]

    def add_units(self, units: int):
        self.units += units

    def remove_units(self, units: int):
        self.units = max(self.units - units, 0)

    def add_price_modifier(self, price_modifier: IPriceModifier):
        self.price_modifiers.append(price_modifier)

    def remove_price_modifier(self, price_modifier: IPriceModifier):
        self.price_modifiers.remove(price_modifier)

    def update_price(self):
        # TODO add modifier that take into account all available gold.
        #  Considering that with all money in game represent price of all resources.
        #  To maintain 1:1 ratio (all gold : all resources price), base price should be modified based on units count of all resources.
        #  Eg. 2 resources, 1 unit each, first base price: 10g, second base price 5g. When first resource is produced and there is 2 units base price should drop.
        #  base_price_of_resource = (all_gold * market_price_representation) / all_units
        #  5g = (15g * 0.66) / 2
        #  5g = (15g * 0.33) / 1
        #  deflation happens, so production of gold is required


        price = self.base_price
        for price_modifier in self.price_modifiers:
            price = price_modifier.modify_price(price)
        self.price_per_unit = price
        self.history_of_price.append(self.price_per_unit)

    def get_gold_equivalent(self) -> int:
        return round(self.base_price * self.units)

