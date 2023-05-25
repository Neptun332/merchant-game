from decimal import Decimal

from EventEngine import EventEngine
from GameEngine import GameEngine
from Map import Map
from market.GlobalMarket import GlobalMarket
from market.Resource import Resource
from market.ResourceName import ResourceName

if __name__ == "__main__":
    resources_map = {
        ResourceName.Wood: Resource(
            name=ResourceName.Wood,
            units=10,
            base_price=Decimal(10),
        ),
        ResourceName.Stone: Resource(
            name=ResourceName.Stone,
            units=10,
            base_price=Decimal(10),
        ),
        ResourceName.Wheat: Resource(
            name=ResourceName.Wheat,
            units=10,
            base_price=Decimal(10),
        ),

    }

    game_engine = GameEngine(
        map=Map(GlobalMarket(), resources_map),
        event_engine=EventEngine(),
        tick_rate=None,
        ticks_to_next_month=30
    )
    game_engine.run()
