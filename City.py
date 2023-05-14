from CityUpgradeStrategy import CityUpgradeStrategy
from market.LocalMarket import LocalMarket
from market.ResourceName import ResourceName
from price_modifiers.UtilityDemandPriceModifier import UtilityDemandPriceModifier


class City:

    # Cities will have production of resources and small production of gold.
    # As the sink of to handle inflation they will be able to spend that on
    # increase of prosperity - strength of economy
    # prosperity:
    # - increases all production
    # - unlocks production of valuable goods

    # This is goiing to be publisher of for example upgrade of city
    # Observer (local market can )

    def __init__(self, name: str, local_market: LocalMarket, upgrade_strategy: CityUpgradeStrategy):
        self.name = name
        self.local_market = local_market
        self.upgrade_strategy = upgrade_strategy
        self.neighbours = {}
        self.prosperity = 100

        # TODO: move to some triggered function when city sets goal to upgrade lvl
        # TODO: create collection with available modifiers
        self.local_market.add_price_modifier(UtilityDemandPriceModifier(), ResourceName.Wood)
        self.local_market.add_price_modifier(UtilityDemandPriceModifier(), ResourceName.Stone)

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

        self.local_market.resources_map[ResourceName.Gold].add_units(1)
        self.local_market.resources_map[ResourceName.Wood].add_units(1)
        self.local_market.resources_map[ResourceName.Stone].add_units(1)
        self.local_market.update(self.upgrade_strategy.get_demand_of_resources())
