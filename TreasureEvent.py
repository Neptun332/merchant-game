import random

from City import City
from Event import Event


class TreasureEvent(Event):
    MESSAGE = "In the City {} found chest with gold. To the treasury was added {}"

    def __init__(self, city: City):
        self.city = city
        self.gold_value = random.randint(100, 200)

    def handle(self):
        self.city.add_gold(self.gold_value)

    def get_message(self) -> str:
        return self.MESSAGE.format(self.city.name, self.gold_value)
