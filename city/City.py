from decimal import Decimal
from typing import Dict, List

from Factor import Factor
from city.CityUpgradeStrategy import CityUpgradeStrategy
from city.ICity import ICity
from event_engine.IEventEngine import IEventEngine
from event_engine.TheftEvent import TheftEvent
from event_engine.config.BaseEventConfig import BaseEventConfig
from market.GlobalMarket import IGlobalMarket
from market.LocalMarket import LocalMarket
from market.ResourceName import ResourceName
from price_modifiers.SupplyDemandPriceModifier import SupplyDemandPriceModifier
from workshop.Workshop import Workshop


class City(ICity):
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
            workshops: List[Workshop],
            event_engine: IEventEngine
    ):
        super().__init__(name, local_market)
        self.global_market = global_market
        self.upgrade_strategy = upgrade_strategy
        self.production_boost = production_boost
        self.workshops = workshops
        self.event_engine = event_engine
        self.neighbours = {}

        self._set_production_origin_of_units()

        # TODO: move to some triggered function when city sets goal to upgrade lvl
        # TODO: create collection with available modifiers
        # TODO: planned modifiers: kingdom regulations
        self.local_market.add_supply_demand_modifier(SupplyDemandPriceModifier(), ResourceName.Wood)
        self.local_market.add_supply_demand_modifier(SupplyDemandPriceModifier(), ResourceName.Stone)

        self.create_theft_event()

    def add_neighbour(self, city: ICity, distance: int):
        self.neighbours.update(
            {
                city: distance
            }
        )

    @staticmethod
    def make_them_neighbours(city_a: ICity, city_b: ICity, distance: int):
        city_a.add_neighbour(city_b, distance)
        city_b.add_neighbour(city_a, distance)

    def update(self, current_tick: int):
        if self.upgrade_strategy.can_upgrade(self.local_market.resources_map):
            resource_needed = self.upgrade_strategy.upgrade()
            [workshop.upgrade() for workshop in self.workshops]
            self.local_market.remove_number_of_resources(resource_needed)

        self._produce_resources(current_tick)
        self._consume_resources()
        self.global_market.update()
        self.local_market.update(self.upgrade_strategy.get_demand_of_resources(), current_tick)

    def show_price_history(self):
        self.local_market.show_price_history(self.name)

    def create_theft_event(self):
        self.event_engine.register_possible_event(
            [TheftEvent(
                city=self,
                event_config=BaseEventConfig((10, 200), TheftEvent.DEFAULT_PROBABILITY),
                event_engine=self.event_engine
            ), ]
        )

    def _produce_resources(self, current_tick: int):
        for workshop in self.workshops:
            if workshop.can_produce(self.local_market.resources_map):
                production_boost = self.production_boost.get(workshop.get_produced_resource_name(), Factor(Decimal(1)))
                consumed_resources, produced_resources = workshop.produce(production_boost, self, current_tick)
                self.local_market.remove_number_of_resources(resource_units=consumed_resources)
                self.local_market.add_resources(resource_units=produced_resources)

    def _consume_resources(self):
        self._consume_food()

    def _consume_food(self):
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
        self.local_market.remove_number_of_resources(food_to_be_consumed)

    def _set_production_origin_of_units(self):
        self.local_market.set_produced_by_on_resource_units(self)
