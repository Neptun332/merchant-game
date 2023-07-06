from abc import ABC, abstractmethod

from market.ILocalMarket import ILocalMarket


class ICity(ABC):

    @abstractmethod
    def __init__(
            self,
            name: str,
            local_market: ILocalMarket
    ):
        self.name = name
        self.local_market = local_market

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

    @abstractmethod
    def create_theft_event(self):
        ...
