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
        ResourceName.GoldOre: Resource(
            name=ResourceName.GoldOre,
            units=0,
        ),
        ResourceName.IronOre: Resource(
            name=ResourceName.IronOre,
            units=10,
        ),
        ResourceName.CopperOre: Resource(
            name=ResourceName.CopperOre,
            units=0,
        ),
        ResourceName.Silk: Resource(
            name=ResourceName.Silk,
            units=0,
        ),
        ResourceName.Fish: Resource(
            name=ResourceName.Fish,
            units=0,
        ),

    }
    resource_gold = Resource(
        name=ResourceName.Gold,
        units=3000,
        base_price=Decimal(1),
    )
    resources_map[ResourceName.Gold] = resource_gold

    global_market = GlobalMarket(
        unit_price_factor_per_resource={
            ResourceName.Wood: Factor(Decimal(.111)),
            ResourceName.Stone: Factor(Decimal(.111)),
            ResourceName.Wheat: Factor(Decimal(.111)),
            ResourceName.IronOre: Factor(Decimal(.111)),
            ResourceName.GoldOre: Factor(Decimal(.111)),
            ResourceName.CopperOre: Factor(Decimal(.111)),
            ResourceName.Silk: Factor(Decimal(.111)),
            ResourceName.Fish: Factor(Decimal(.111)),
        }
    )

    game_engine = GameEngine(
        map=Map(global_market),
        event_engine=EventEngine(),
        tick_rate=None,
        ticks_to_next_month=30,
        global_market=global_market
    )
    game_engine.run()
