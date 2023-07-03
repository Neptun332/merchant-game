import sys
from typing import List

from market.ResourceName import ResourceName
from workshop.ConsumingWorkshop import ConsumingWorkshop
from workshop.NotConsumingWorkshop import NotConsumingWorkshop
from workshop.Workshop import Workshop


def generate_workshops_for_city_a() -> List[Workshop]:
    return [
        NotConsumingWorkshop(
            resource_name_produced=ResourceName.Wood,
            resource_units_produced=1,
            level=3,
            produced_unit_ticks_lifetime=sys.maxsize,
        ),
        NotConsumingWorkshop(
            resource_name_produced=ResourceName.Stone,
            resource_units_produced=1,
            level=1,
            produced_unit_ticks_lifetime=sys.maxsize,
        ),
        NotConsumingWorkshop(
            resource_name_produced=ResourceName.Wheat,
            resource_units_produced=1,
            level=2,
        ),
        NotConsumingWorkshop(
            resource_name_produced=ResourceName.IronOre,
            resource_units_produced=1,
            level=1,
        ),
    ]


def generate_workshops_for_city_b() -> List[Workshop]:
    return [
        NotConsumingWorkshop(
            resource_name_produced=ResourceName.Wood,
            resource_units_produced=1,
            level=1,
            produced_unit_ticks_lifetime=sys.maxsize,
        ),
        NotConsumingWorkshop(
            resource_name_produced=ResourceName.Stone,
            resource_units_produced=1,
            level=3,
            produced_unit_ticks_lifetime=sys.maxsize,
        ),
        NotConsumingWorkshop(
            resource_name_produced=ResourceName.Wheat,
            resource_units_produced=1,
            level=2,
        ),
        NotConsumingWorkshop(
            resource_name_produced=ResourceName.IronOre,
            resource_units_produced=1,
            level=2,
        ),
        NotConsumingWorkshop(
            resource_name_produced=ResourceName.CopperOre,
            resource_units_produced=1,
            level=1,
        ),
    ]


def generate_workshops_for_city_c() -> List[Workshop]:
    return [
        NotConsumingWorkshop(
            resource_name_produced=ResourceName.Wood,
            resource_units_produced=1,
            level=1,
            produced_unit_ticks_lifetime=sys.maxsize,
        ),
        NotConsumingWorkshop(
            resource_name_produced=ResourceName.Stone,
            resource_units_produced=1,
            level=1,
            produced_unit_ticks_lifetime=sys.maxsize,
        ),
        NotConsumingWorkshop(
            resource_name_produced=ResourceName.Wheat,
            resource_units_produced=1,
            level=3,
        ),
        NotConsumingWorkshop(
            resource_name_produced=ResourceName.GoldOre,
            resource_units_produced=1,
            level=3,
            produced_unit_ticks_lifetime=sys.maxsize,
        ),
        ConsumingWorkshop(
            resource_name_produced=ResourceName.Gold,
            resource_units_produced=100,
            resource_name_consumed=ResourceName.GoldOre,
            resource_units_consumed=1,
            level=1,
            produced_unit_ticks_lifetime=sys.maxsize,
        ),
    ]


def generate_workshops_for_city_d() -> List[Workshop]:
    return [
        NotConsumingWorkshop(
            resource_name_produced=ResourceName.Wood,
            resource_units_produced=1,
            level=1,
            produced_unit_ticks_lifetime=sys.maxsize,
        ),
        NotConsumingWorkshop(
            resource_name_produced=ResourceName.Stone,
            resource_units_produced=1,
            level=1,
            produced_unit_ticks_lifetime=sys.maxsize,
        ),
        NotConsumingWorkshop(
            resource_name_produced=ResourceName.Wheat,
            resource_units_produced=1,
            level=2,
        ),
        NotConsumingWorkshop(
            resource_name_produced=ResourceName.Silk,
            resource_units_produced=1,
            level=1,
        ),
        NotConsumingWorkshop(
            resource_name_produced=ResourceName.Fish,
            resource_units_produced=1,
            level=2,
        ),
    ]


def generate_workshops_for_city_e() -> List[Workshop]:
    return [
        NotConsumingWorkshop(
            resource_name_produced=ResourceName.Wood,
            resource_units_produced=1,
            level=1,
            produced_unit_ticks_lifetime=sys.maxsize,
        ),
        NotConsumingWorkshop(
            resource_name_produced=ResourceName.Stone,
            resource_units_produced=1,
            level=1,
            produced_unit_ticks_lifetime=sys.maxsize,
        ),
        NotConsumingWorkshop(
            resource_name_produced=ResourceName.Wheat,
            resource_units_produced=2,
            level=2,
        ),
        NotConsumingWorkshop(
            resource_name_produced=ResourceName.Silk,
            resource_units_produced=1,
            level=2,
        ),
        NotConsumingWorkshop(
            resource_name_produced=ResourceName.Fish,
            resource_units_produced=1,
            level=1,
        ),
    ]
