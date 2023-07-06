from decimal import Decimal

from event_engine.EventEngine import EventEngine
from Factor import Factor
from GameEngine import GameEngine
from Map import Map
from market.GlobalMarket import GlobalMarket
from market.ResourceName import ResourceName

if __name__ == "__main__":
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

    event_engine = EventEngine()
    game_engine = GameEngine(
        map=Map(global_market, event_engine),
        event_engine=event_engine,
        tick_rate=None,
        ticks_to_next_month=30,
        global_market=global_market
    )
    game_engine.run()
