from abc import ABC
from typing import List

from City import City
from Factor import Factor


class IGlobalMarket(ABC):
    pass


class GlobalMarket(IGlobalMarket):

    def __init__(self):
        self.cities = []
        self.last_sum_of_gold = self.get_sum_of_gold_in_every_city(self.cities)

    def set_cities(self, cities: List[City]):
        self.cities = cities

    def get_sum_of_gold_in_every_city(self, cities: List[City]):
        return sum([city.resources.gold for city in cities])

    def update(self):
        inflation = self.calculate_inflation()

    def calculate_inflation(self) -> Factor:
        sum_of_gold = self.get_sum_of_gold_in_every_city(self.cities)
        return Factor(1 - (sum_of_gold / self.last_sum_of_gold))
