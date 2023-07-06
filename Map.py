from typing import Set

from Kingdom import Kingdom
from city.City import City
from event_engine.IEventEngine import IEventEngine
from market.GlobalMarket import IGlobalMarket
from utils.city_generation import generate_city_a, generate_city_b, generate_city_c, generate_city_d, generate_city_e


class Map:

    def __init__(self, global_market: IGlobalMarket, event_engine: IEventEngine):
        self._global_market = global_market
        self._event_engine = event_engine
        self._create_hardcoded_kingdoms_with_cities()

    def _create_hardcoded_kingdoms_with_cities(self):
        a = generate_city_a(self._global_market, self._event_engine)
        b = generate_city_b(self._global_market, self._event_engine)
        c = generate_city_c(self._global_market, self._event_engine)
        d = generate_city_d(self._global_market, self._event_engine)
        e = generate_city_e(self._global_market, self._event_engine)

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
