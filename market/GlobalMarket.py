from abc import ABC, abstractmethod
from typing import List

from City import City
from Percentage import Percentage
from market.ResourcesPrice import ResourcesPrice


class IGlobalMarket(ABC):

    @abstractmethod
    def get_recourses_prices(self):
        pass


class GlobalMarket(IGlobalMarket):

    def __init__(self, base_resources_price: ResourcesPrice):
        self.cities = []
        self.last_sum_of_gold = self.get_sum_of_gold_in_every_city(self.cities)
        self.resources_price = base_resources_price

    def set_cities(self, cities: List[City]):
        self.cities = cities

    def get_sum_of_gold_in_every_city(self, cities: List[City]):
        return sum([city.resources.gold for city in cities])

    def update(self):
        inflation = self.calculate_inflation()
        self.resources_price.increase_price_of_all_by_percentage(inflation)

    def calculate_inflation(self) -> Percentage:
        sum_of_gold = self.get_sum_of_gold_in_every_city(self.cities)
        return Percentage(1 - (sum_of_gold / self.last_sum_of_gold))

    def get_recourses_prices(self) -> ResourcesPrice:
        return self.resources_price
