import sys
from typing import Dict, List

from market.Resource import Resource
from market.ResourceName import ResourceName
from market.Unit import Unit


def generate_number_of_units(number_of_units: int) -> List[Unit]:
    return [
        Unit(
            ttl=Unit.DEFAULT_UNIT_LIFE_TIME,
            produced_by=None
        ) for _ in range(number_of_units)
    ]


def generate_number_of_not_expiring_units(number_of_units: int) -> List[Unit]:
    return [
        Unit(
            ttl=sys.maxsize,
            produced_by=None
        ) for _ in range(number_of_units)
    ]


def generate_resources_for_city_a() -> Dict[ResourceName, Resource]:
    return {
        ResourceName.Wood: Resource(
            name=ResourceName.Wood,
            units=generate_number_of_units(200),
        ),
        ResourceName.Stone: Resource(
            name=ResourceName.Stone,
            units=generate_number_of_units(50),
        ),
        ResourceName.Wheat: Resource(
            name=ResourceName.Wheat,
            units=generate_number_of_units(105),
        ),
        ResourceName.GoldOre: Resource(
            name=ResourceName.GoldOre,
            units=generate_number_of_units(0),
        ),
        ResourceName.IronOre: Resource(
            name=ResourceName.IronOre,
            units=generate_number_of_units(10),
        ),
        ResourceName.CopperOre: Resource(
            name=ResourceName.CopperOre,
            units=generate_number_of_units(0),
        ),
        ResourceName.Silk: Resource(
            name=ResourceName.Silk,
            units=generate_number_of_units(0),
        ),
        ResourceName.Fish: Resource(
            name=ResourceName.Fish,
            units=generate_number_of_units(0),
        ),
        ResourceName.Gold: Resource(
            name=ResourceName.Gold,
            units=generate_number_of_not_expiring_units(5000),
        )
    }


def generate_resources_for_city_b() -> Dict[ResourceName, Resource]:
    return {
        ResourceName.Wood: Resource(
            name=ResourceName.Wood,
            units=generate_number_of_units(55),
        ),
        ResourceName.Stone: Resource(
            name=ResourceName.Stone,
            units=generate_number_of_units(203),
        ),
        ResourceName.Wheat: Resource(
            name=ResourceName.Wheat,
            units=generate_number_of_units(116),
        ),
        ResourceName.GoldOre: Resource(
            name=ResourceName.GoldOre,
            units=generate_number_of_units(0),
        ),
        ResourceName.IronOre: Resource(
            name=ResourceName.IronOre,
            units=generate_number_of_units(112),
        ),
        ResourceName.CopperOre: Resource(
            name=ResourceName.CopperOre,
            units=generate_number_of_units(30),
        ),
        ResourceName.Silk: Resource(
            name=ResourceName.Silk,
            units=generate_number_of_units(0),
        ),
        ResourceName.Fish: Resource(
            name=ResourceName.Fish,
            units=generate_number_of_units(0),
        ),
        ResourceName.Gold: Resource(
            name=ResourceName.Gold,
            units=generate_number_of_not_expiring_units(5500),
        )
    }


def generate_resources_for_city_c() -> Dict[ResourceName, Resource]:
    return {
        ResourceName.Wood: Resource(
            name=ResourceName.Wood,
            units=generate_number_of_units(118),
        ),
        ResourceName.Stone: Resource(
            name=ResourceName.Stone,
            units=generate_number_of_units(92),
        ),
        ResourceName.Wheat: Resource(
            name=ResourceName.Wheat,
            units=generate_number_of_units(150),
        ),
        ResourceName.GoldOre: Resource(
            name=ResourceName.GoldOre,
            units=generate_number_of_units(210),
        ),
        ResourceName.IronOre: Resource(
            name=ResourceName.IronOre,
            units=generate_number_of_units(0),
        ),
        ResourceName.CopperOre: Resource(
            name=ResourceName.CopperOre,
            units=generate_number_of_units(0),
        ),
        ResourceName.Silk: Resource(
            name=ResourceName.Silk,
            units=generate_number_of_units(0),
        ),
        ResourceName.Fish: Resource(
            name=ResourceName.Fish,
            units=generate_number_of_units(0),
        ),
        ResourceName.Gold: Resource(
            name=ResourceName.Gold,
            units=generate_number_of_not_expiring_units(10000),
        )
    }


def generate_resources_for_city_d() -> Dict[ResourceName, Resource]:
    return {
        ResourceName.Wood: Resource(
            name=ResourceName.Wood,
            units=generate_number_of_units(125),
        ),
        ResourceName.Stone: Resource(
            name=ResourceName.Stone,
            units=generate_number_of_units(70),
        ),
        ResourceName.Wheat: Resource(
            name=ResourceName.Wheat,
            units=generate_number_of_units(80),
        ),
        ResourceName.GoldOre: Resource(
            name=ResourceName.GoldOre,
            units=generate_number_of_units(0),
        ),
        ResourceName.IronOre: Resource(
            name=ResourceName.IronOre,
            units=generate_number_of_units(0),
        ),
        ResourceName.CopperOre: Resource(
            name=ResourceName.CopperOre,
            units=generate_number_of_units(0),
        ),
        ResourceName.Silk: Resource(
            name=ResourceName.Silk,
            units=generate_number_of_units(50),
        ),
        ResourceName.Fish: Resource(
            name=ResourceName.Fish,
            units=generate_number_of_units(97),
        ),
        ResourceName.Gold: Resource(
            name=ResourceName.Gold,
            units=generate_number_of_not_expiring_units(5700),
        )
    }


def generate_resources_for_city_e() -> Dict[ResourceName, Resource]:
    return {
        ResourceName.Wood: Resource(
            name=ResourceName.Wood,
            units=generate_number_of_units(140),
        ),
        ResourceName.Stone: Resource(
            name=ResourceName.Stone,
            units=generate_number_of_units(50),
        ),
        ResourceName.Wheat: Resource(
            name=ResourceName.Wheat,
            units=generate_number_of_units(85),
        ),
        ResourceName.GoldOre: Resource(
            name=ResourceName.GoldOre,
            units=generate_number_of_units(0),
        ),
        ResourceName.IronOre: Resource(
            name=ResourceName.IronOre,
            units=generate_number_of_units(0),
        ),
        ResourceName.CopperOre: Resource(
            name=ResourceName.CopperOre,
            units=generate_number_of_units(0),
        ),
        ResourceName.Silk: Resource(
            name=ResourceName.Silk,
            units=generate_number_of_units(105),
        ),
        ResourceName.Fish: Resource(
            name=ResourceName.Fish,
            units=generate_number_of_units(50),
        ),
        ResourceName.Gold: Resource(
            name=ResourceName.Gold,
            units=generate_number_of_not_expiring_units(5600),
        )
    }
