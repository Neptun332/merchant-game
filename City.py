from Resources import Resources


class City:

    # Cities will have production of resources and small production of gold.
    # As the sink of to handle inflation they will be able to spend that on
    # increase of prosperity - strength of economy
    # prosperity:
    # - increases all production
    # - unlocks production of valuable goods

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
