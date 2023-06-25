from decimal import Decimal

from EventEngine import EventEngine
from Factor import Factor
from GameEngine import GameEngine
from Map import Map
from market.GlobalMarket import GlobalMarket
from market.Resource import Resource
from market.ResourceName import ResourceName

if __name__ == "__main__":
    resources_map = {
        ResourceName.Wood: Resource(
            name=ResourceName.Wood,
            units=100,
        ),
        ResourceName.Stone: Resource(
            name=ResourceName.Stone,
            units=100,
        ),
        ResourceName.Wheat: Resource(
            name=ResourceName.Wheat,
            units=100,
        ),
        ResourceName.IronOre: Resource(
            name=ResourceName.IronOre,
            units=10,
        ),
    }
    resource_gold = Resource(
        name=ResourceName.Gold,
        units=3000,
        base_price=Decimal(1),
    )
    resources_map[ResourceName.Gold] = resource_gold

    game_engine = GameEngine(
        map=Map(GlobalMarket(
            unit_price_factor_per_resource={
                ResourceName.Wood: Factor(Decimal(.25)),
                ResourceName.Stone: Factor(Decimal(.25)),
                ResourceName.Wheat: Factor(Decimal(.25)),
                ResourceName.IronOre: Factor(Decimal(.25)),
                ResourceName.GoldOre: Factor(Decimal(0)),
                ResourceName.CopperOre: Factor(Decimal(0)),
                ResourceName.Silk: Factor(Decimal(0)),
                ResourceName.Fish: Factor(Decimal(0)),
            }
        ), resources_map),
        event_engine=EventEngine(),
        tick_rate=None,
        ticks_to_next_month=30
    )
    game_engine.run()
