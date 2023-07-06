from typing import Set

from city.ICity import ICity


class Kingdom:

    def __init__(self, name: str, cities: Set[ICity]):
        self.name = name
        self.cities = cities
