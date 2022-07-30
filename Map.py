from typing import Set

from City import City
from Kingdom import Kingdom
from market.GlobalMarket import IGlobalMarket
from market.LocalMarket import LocalMarket


class Map:

    def __init__(self, global_market: IGlobalMarket):
        self._global_market = global_market
        self._create_hardcoded_kingdoms_with_cities()

    def _create_hardcoded_kingdoms_with_cities(self):
        resources_price = self._global_market.get_recourses_prices()
        a = City("A", LocalMarket(resources_price))
        b = City("B", LocalMarket(resources_price))
        c = City("C", LocalMarket(resources_price))
        d = City("D", LocalMarket(resources_price))
        e = City("E", LocalMarket(resources_price))

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
