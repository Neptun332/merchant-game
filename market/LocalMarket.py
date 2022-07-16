from City import City
from market.GlobalMarket import IGlobalMarket
from market.ResourcesPrice import ResourcesPrice


class LocalMarket:

    def __init__(self, global_market: IGlobalMarket, city: City):
        self.global_market = global_market
        self.resources_price = ResourcesPrice()
