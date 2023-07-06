from abc import ABC, abstractmethod
from decimal import Decimal
from typing import Dict, List

from market.Resource import Resource
from market.ResourceName import ResourceName
from market.Unit import Unit
from price_modifiers.IPriceModifier import IPriceModifier


class ILocalMarket(ABC):
    @abstractmethod
    def __init__(
            self,
            resources_map: Dict[ResourceName, Resource],
    ):
        self.resources_map = resources_map

    @abstractmethod
    def update(self, demand: Dict[ResourceName, int], current_tick: int):
        ...

    @abstractmethod
    def remove_number_of_resources(self, resource_units: Dict[ResourceName, int]):
        ...

    @abstractmethod
    def add_resources(self, resource_units: Dict[ResourceName, List[Unit]]):
        ...

    @abstractmethod
    def get_resource_units(self, resource_name: ResourceName):
        ...

    @abstractmethod
    def add_supply_demand_modifier(self, price_modifier: IPriceModifier, resource_name: ResourceName):
        ...

    @abstractmethod
    def remove_supply_demand_modifier(self, resource_name: ResourceName):
        ...

    # TODO move it to dedicated class
    @abstractmethod
    def show_price_history(self, city_name: str):
        ...

    @abstractmethod
    def set_resource_base_price(self, base_price: Decimal, resource_name: ResourceName):
        ...

    # @abstractmethod
    # def set_produced_by_on_resource_units(self, produced_by: ICity):
    #     ...
