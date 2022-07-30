from decimal import Decimal

from EventEngine import EventEngine
from GameEngine import GameEngine
from Map import Map
from market.GlobalMarket import GlobalMarket
from market.ResourcesPrice import ResourcesPrice

if __name__ == "__main__":
    game_engine = GameEngine(
        map=Map(GlobalMarket(ResourcesPrice(Decimal(100), Decimal(100), Decimal(100)))),
        event_engine=EventEngine(),
        tick_rate=1
    )
    game_engine.run()
