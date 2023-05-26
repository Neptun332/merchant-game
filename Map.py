import copy
from decimal import Decimal
from typing import Set, Dict

from City import City
from CityUpgradeStrategy import CityUpgradeStrategy
from Factor import Factor
from Kingdom import Kingdom
from market.GlobalMarket import IGlobalMarket
from market.LocalMarket import LocalMarket
from market.Resource import Resource
from market.ResourceName import ResourceName


class Map:

    def __init__(self, global_market: IGlobalMarket, resources_price: Dict[ResourceName, Resource]):
        self._global_market = global_market
        self._create_hardcoded_kingdoms_with_cities(resources_price)

    def _create_hardcoded_kingdoms_with_cities(self, resources_map: Dict[ResourceName, Resource]):
        # TODO add Factory Method or even abstract factory for creating cities
        upgrade_strategy = CityUpgradeStrategy(
            resources_needed={
                ResourceName.Wood: 100,
                ResourceName.Stone: 100,
            },
            gold_needed=Decimal(100)
        )
        a = City(
            name="A",
            local_market=LocalMarket(
                resources_map=copy.deepcopy(resources_map),
                gold=Decimal(100)
            ),
            upgrade_strategy=copy.deepcopy(upgrade_strategy),
            produced_resources=[ResourceName.Wood, ResourceName.Stone, ResourceName.Wheat, ResourceName.IronOre],
            production_boost={ResourceName.Wood: Factor(Decimal('1.2'))}
        )
        b = City(
            name="B",
            local_market=LocalMarket(
                resources_map=copy.deepcopy(resources_map),
                gold=Decimal(100)
            ),
            upgrade_strategy=copy.deepcopy(upgrade_strategy),
            produced_resources=[ResourceName.Wood, ResourceName.Stone, ResourceName.Wheat],
            production_boost={}
        )
        c = City(
            name="C",
            local_market=LocalMarket(
                resources_map=copy.deepcopy(resources_map),
                gold=Decimal(100)
            ),
            upgrade_strategy=copy.deepcopy(upgrade_strategy),
            produced_resources=[ResourceName.Wood, ResourceName.Stone, ResourceName.Wheat],
            production_boost={}
        )
        d = City(
            name="D",
            local_market=LocalMarket(
                resources_map=copy.deepcopy(resources_map),
                gold=Decimal(100)
            ),
            upgrade_strategy=copy.deepcopy(upgrade_strategy),
            produced_resources=[ResourceName.Wood, ResourceName.Stone, ResourceName.Wheat],
            production_boost={}
        )
        e = City(
            name="E",
            local_market=LocalMarket(
                resources_map=copy.deepcopy(resources_map),
                gold=Decimal(100)
            ),
            upgrade_strategy=copy.deepcopy(upgrade_strategy),
            produced_resources=[ResourceName.Wood, ResourceName.Stone, ResourceName.Wheat],
            production_boost={}
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

    def get_cities(self) -> Set[City]:
        return self.cities
