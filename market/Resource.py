from dataclasses import dataclass, field
from decimal import Decimal
from typing import List

from market.ResourceName import ResourceName
from market.Unit import Unit
from price_modifiers.IPriceModifier import IPriceModifier


@dataclass
class Resource:
    name: ResourceName
    units: List[Unit]
    base_price: Decimal = None
    price_per_unit: Decimal = None
    history_of_price: List = field(default_factory=lambda: [])
    price_modifiers: List = field(default_factory=list)

    def __post_init__(self):
        self.price_per_unit = self.base_price
        self.history_of_price = [self.price_per_unit]

    def add_units(self, units: List[Unit]):
        self.units += units

    def remove_number_of_units(self, units_count: int):
        self.units = sorted(self.units, key=lambda x: x.ttl)
        if not units_count:
            pass
        del self.units[0:units_count]

    def add_price_modifier(self, price_modifier: IPriceModifier):
        self.price_modifiers.append(price_modifier)

    def remove_price_modifier(self, price_modifier: IPriceModifier):
        self.price_modifiers.remove(price_modifier)

    def get_units_count(self) -> int:
        return len(self.units)

    def update_price(self):
        price = self.base_price
        for price_modifier in self.price_modifiers:
            price = price_modifier.modify_price(price)
        self.price_per_unit = price
        self.history_of_price.append(self.price_per_unit)

    def get_gold_equivalent(self) -> int:
        return round(self.price_per_unit * len(self.units))

    def remove_expired_units(self, current_tick: int):
        self.units = [unit for unit in self.units if unit.get_ttl() > current_tick]
