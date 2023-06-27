import copy
from decimal import Decimal
from typing import Set, Dict

from Factor import Factor
from Kingdom import Kingdom
from city.City import City
from city.CityUpgradeStrategy import CityUpgradeStrategy
from market.GlobalMarket import IGlobalMarket
from market.LocalMarket import LocalMarket
from market.Resource import Resource
from market.ResourceName import ResourceName
from workshop.NotConsumingWorkshop import NotConsumingWorkshop


class Map:

    def __init__(self, global_market: IGlobalMarket, resources_price: Dict[ResourceName, Resource]):
        self._global_market = global_market
        self._create_hardcoded_kingdoms_with_cities(resources_price)

    def _create_hardcoded_kingdoms_with_cities(self, resources_map: Dict[ResourceName, Resource]):
        # TODO add Factory Method or even abstract factory for creating cities
        upgrade_strategy = CityUpgradeStrategy(
            resources_needed={
                ResourceName.Wood: 100,
                ResourceName.Stone: 100
            },
        )
        basic_workshops = [
            NotConsumingWorkshop(
                resource_name_produced=ResourceName.Wood,
                resource_units_produced=1,
                city_level=upgrade_strategy.get_city_level(),
            ),
            NotConsumingWorkshop(
                resource_name_produced=ResourceName.Stone,
                resource_units_produced=1,
                city_level=upgrade_strategy.get_city_level(),
            ),
            NotConsumingWorkshop(
                resource_name_produced=ResourceName.Wheat,
                resource_units_produced=1,
                city_level=upgrade_strategy.get_city_level(),
            ),

        ]

        a = City(
            name="A",
            local_market=LocalMarket(
                resources_map=copy.deepcopy(resources_map),
            ),
            global_market=self._global_market,
            upgrade_strategy=copy.deepcopy(upgrade_strategy),
            produced_resources=[ResourceName.Wood, ResourceName.Stone, ResourceName.Wheat, ResourceName.IronOre],
            production_boost={ResourceName.Wood: Factor(Decimal('1.2'))},
            workshops=basic_workshops
        )
        b = City(
            name="B",
            local_market=LocalMarket(
                resources_map=copy.deepcopy(resources_map),
            ),
            global_market=self._global_market,
            upgrade_strategy=copy.deepcopy(upgrade_strategy),
            produced_resources=[ResourceName.Wood, ResourceName.Stone, ResourceName.Wheat],
            production_boost={},
            workshops=basic_workshops

        )
        c = City(
            name="C",
            local_market=LocalMarket(
                resources_map=copy.deepcopy(resources_map),
            ),
            global_market=self._global_market,
            upgrade_strategy=copy.deepcopy(upgrade_strategy),
            produced_resources=[ResourceName.Wood, ResourceName.Stone, ResourceName.Wheat],
            production_boost={},
            workshops=basic_workshops
        )
        d = City(
            name="D",
            local_market=LocalMarket(
                resources_map=copy.deepcopy(resources_map),
            ),
            global_market=self._global_market,
            upgrade_strategy=copy.deepcopy(upgrade_strategy),
            produced_resources=[ResourceName.Wood, ResourceName.Stone, ResourceName.Wheat],
            production_boost={},
            workshops=basic_workshops
        )
        e = City(
            name="E",
            local_market=LocalMarket(
                resources_map=copy.deepcopy(resources_map),
            ),
            global_market=self._global_market,
            upgrade_strategy=copy.deepcopy(upgrade_strategy),
            produced_resources=[ResourceName.Wood, ResourceName.Stone, ResourceName.Wheat],
            production_boost={},
            workshops=basic_workshops
        )

        City.make_them_neighbours(a, b, 10)
        City.make_them_neighbours(a, c, 12)
        City.make_them_neighbours(b, c, 5)
        City.make_them_neighbours(b, e, 13)
        City.make_them_neighbours(b, d, 11)
        City.make_them_neighbours(e, d, 6)
        #           E
        #         / |
        #        /  |
        # A -- B -- D
        #   \  |
        #    \ |
        #      C
        self.kingdoms = {
            Kingdom(name="Left", cities={a, c}),
            Kingdom(name="Central", cities={b}),
            Kingdom(name="Right", cities={d, e})
        }

        self.cities = {
            a,
            b,
            c,
            d,
            e
        }

        self._global_market.set_local_markets(
            local_markets={
                id(city.local_market): city.local_market
                for city in self.cities
            }
        )

    def get_cities(self) -> Set[City]:
        return self.cities
