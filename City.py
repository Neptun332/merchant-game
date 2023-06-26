from decimal import Decimal
from typing import Dict, List

from CityUpgradeStrategy import CityUpgradeStrategy
from Factor import Factor
from Workshop import Workshop
from market.GlobalMarket import IGlobalMarket
from market.LocalMarket import LocalMarket
from market.ResourceName import ResourceName
from price_modifiers.UtilityDemandPriceModifier import UtilityDemandPriceModifier


class City:
    FOOD_RESOURCES = [ResourceName.Wheat, ResourceName.Fish]

    # Cities will have production of resources and small production of gold.
    # As the sink of to handle inflation they will be able to spend that on
    # increase of prosperity - strength of economy
    # prosperity:
    # - increases all production
    # - unlocks production of valuable goods

    # This is goiing to be publisher of for example upgrade of city
    # Observer (local market can )

    def __init__(
            self,
            name: str,
            local_market: LocalMarket,
            global_market: IGlobalMarket,
            upgrade_strategy: CityUpgradeStrategy,
            produced_resources: List[ResourceName],
            production_boost: Dict[ResourceName, Factor],
            workshops: List[Workshop] = []
    ):
        self.name = name
        self.local_market = local_market
        self.global_market = global_market
        self.upgrade_strategy = upgrade_strategy
        self.produced_resources = produced_resources
        self.production_boost = production_boost
        self.workshops = workshops
        self.neighbours = {}

        # TODO: move to some triggered function when city sets goal to upgrade lvl
        # TODO: create collection with available modifiers
        # TODO: planned modifiers: kingdom regulations
        self.local_market.add_utility_demand_modifier(UtilityDemandPriceModifier(), ResourceName.Wood)
        self.local_market.add_utility_demand_modifier(UtilityDemandPriceModifier(), ResourceName.Stone)

    def add_neighbour(self, city: 'City', distance: int):
        self.neighbours.update(
            {
                city: distance
            }
        )

    @staticmethod
    def make_them_neighbours(city_a: 'City', city_b: 'City', distance: int):
        city_a.add_neighbour(city_b, distance)
        city_b.add_neighbour(city_a, distance)

    def update(self):
        if self.upgrade_strategy.can_upgrade(self.local_market.resources_map):
            resource_needed = self.upgrade_strategy.upgrade()
            self.local_market.remove_resources(resource_needed)

        self.produce_resources()
        self.consume_resources()
        self.global_market.update()
        self.local_market.update(self.upgrade_strategy.get_demand_of_resources())

    def produce_resources(self):
        base_production = self.upgrade_strategy.get_prosperity() / 100
        for resource_name in self.produced_resources:
            production = base_production * float(self.production_boost.get(resource_name, Factor(Decimal(1))).value)
            self.local_market.resources_map[resource_name].add_units(int(production))

    def consume_resources(self):
        self.consume_food()

    def consume_food(self):
        base_consumption = self.upgrade_strategy.get_prosperity() / 100
        food_resources_units = {
            resource_name: self.local_market.get_resource_units(resource_name)
            for resource_name in self.FOOD_RESOURCES
        }
        all_food_units = sum(food_resources_units.values())
        food_to_be_consumed = {
            resource_name: round(base_consumption * (food_resources_units[resource_name] / all_food_units))
            for resource_name in self.FOOD_RESOURCES
        }
        self.local_market.remove_resources(food_to_be_consumed)
