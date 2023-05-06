from CityUpgradeStrategy import CityUpgradeStrategy
from market.LocalMarket import LocalMarket
from market.ResourceName import ResourceName


class City:

    # Cities will have production of resources and small production of gold.
    # As the sink of to handle inflation they will be able to spend that on
    # increase of prosperity - strength of economy
    # prosperity:
    # - increases all production
    # - unlocks production of valuable goods

    def __init__(self, name: str, local_market: LocalMarket, upgrade_strategy: CityUpgradeStrategy):
        self.name = name
        self.local_market = local_market
        self.upgrade_strategy = upgrade_strategy
        self.neighbours = {}
        self.prosperity = 100

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
        self.local_market.resources_map = self.upgrade_strategy.upgrade(self.local_market.resources_map)
        self.local_market.resources_map[ResourceName.Gold].add_units(1)
        self.local_market.resources_map[ResourceName.Wood].add_units(1)
        self.local_market.resources_map[ResourceName.Stone].add_units(1)
        self.local_market.update(self.upgrade_strategy.get_demand_of_resources(self.local_market.resources_map))
