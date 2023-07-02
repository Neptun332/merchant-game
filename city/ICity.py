from abc import ABC, abstractmethod


class ICity(ABC):
    @abstractmethod
    def add_neighbour(self, city: 'ICity', distance: int):
        ...

    @staticmethod
    @abstractmethod
    def make_them_neighbours(city_a: 'ICity', city_b: 'ICity', distance: int):
        ...

    @abstractmethod
    def update(self, current_tick: int):
        ...

    @abstractmethod
    def show_price_history(self):
        ...
