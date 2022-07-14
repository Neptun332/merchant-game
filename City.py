from Resources import Resources


class City:

    def __init__(self, name: str):
        self.name = name
        self.neighbours = {}
        self.resources = Resources(
            gold=300,
            wheat=100,
            wood=100,
            stone=100,
        )

    def add_neighbour(self, city: 'City', distance: int):
        self.neighbours.update(
            {
                city: distance
            }
        )

    @staticmethod
    def make_them_neighbours(city_a: 'City', city_b: 'City', distance: int):
        city_a.add_neighbour(city_b, distance)
        city_b.add_neighbour(city_a, distance)

    def add_gold(self, value: int):
        self.resources.gold += value
