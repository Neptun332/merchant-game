from decimal import Decimal
from typing import Dict, List

from Factor import Factor
from city.CityUpgradeStrategy import CityUpgradeStrategy
from market.GlobalMarket import IGlobalMarket
from market.LocalMarket import LocalMarket
from market.ResourceName import ResourceName
from price_modifiers.UtilityDemandPriceModifier import UtilityDemandPriceModifier
from workshop.Workshop import Workshop


class City:
    FOOD_RESOURCES = [ResourceName.Wheat, ResourceName.Fish]

    # Cities will have production of resources and small production of gold.
    # increase of prosperity - strength of economy
    # prosperity:
    # - increases all production
    # - unlocks production of valuable goods

    def __init__(
            self,
            name: str,
            local_market: LocalMarket,
            global_market: IGlobalMarket,
            upgrade_strategy: CityUpgradeStrategy,
            production_boost: Dict[ResourceName, Factor],
            workshops: List[Workshop] = []
    ):
        self.name = name
        self.local_market = local_market
        self.global_market = global_market
        self.upgrade_strategy = upgrade_strategy
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
            [workshop.upgrade() for workshop in self.workshops]
            self.local_market.remove_resources(resource_needed)

        self.produce_resources()
        self.consume_resources()
        self.global_market.update()
        self.local_market.update(self.upgrade_strategy.get_demand_of_resources())

    def produce_resources(self):
        for workshop in self.workshops:
            if workshop.can_produce(self.local_market.resources_map):
                production_boost = self.production_boost.get(workshop.get_produced_resource_name(), Factor(Decimal(1)))
                consumed_resources, produced_resources = workshop.produce(production_boost)
                self.local_market.remove_resources(resource_units=consumed_resources)
                self.local_market.add_resources(resource_units=produced_resources)

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

    def show_price_history(self):
        self.local_market.show_price_history(self.name)
