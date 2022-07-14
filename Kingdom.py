from typing import Set

from City import City


class Kingdom:

    def __init__(self, name: str, cities: Set[City]):
        self.name = name
        self.cities = cities
