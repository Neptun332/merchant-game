from typing import Set

from City import City
from Kingdom import Kingdom


class Map:

    def __init__(self):
        self._create_hardcoded_kingdoms_with_cities()

    def _create_hardcoded_kingdoms_with_cities(self):
        a = City("A")
        b = City("B")
        c = City("C")
        d = City("D")
        e = City("E")

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
