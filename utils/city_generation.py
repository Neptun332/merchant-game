from decimal import Decimal

from Factor import Factor
from city.City import City
from city.CityUpgradeStrategy import CityUpgradeStrategy
from market.GlobalMarket import IGlobalMarket
from market.LocalMarket import LocalMarket
from market.ResourceName import ResourceName
from utils.resource_generation import generate_resources_for_city_a, generate_resources_for_city_b, \
    generate_resources_for_city_c, generate_resources_for_city_d, generate_resources_for_city_e
from utils.workshop_generation import generate_workshops_for_city_a, generate_workshops_for_city_b, \
    generate_workshops_for_city_c, generate_workshops_for_city_d, generate_workshops_for_city_e


def generate_city_a(global_market: IGlobalMarket) -> City:
    return City(
        name="A",
        local_market=LocalMarket(
            resources_map=generate_resources_for_city_a(),
        ),
        global_market=global_market,
        upgrade_strategy=CityUpgradeStrategy(
            resources_needed={
                ResourceName.Wood: 100,
                ResourceName.Stone: 100
            },
        ),
        production_boost={ResourceName.Wood: Factor(Decimal('1.2'))},
        workshops=generate_workshops_for_city_a()
    )


def generate_city_b(global_market: IGlobalMarket) -> City:
    return City(
        name="B",
        local_market=LocalMarket(
            resources_map=generate_resources_for_city_b(),
        ),
        global_market=global_market,
        upgrade_strategy=CityUpgradeStrategy(
            resources_needed={
                ResourceName.Wood: 100,
                ResourceName.Stone: 100
            },
        ),
        production_boost={ResourceName.IronOre: Factor(Decimal('1.2'))},
        workshops=generate_workshops_for_city_b()
    )


def generate_city_c(global_market: IGlobalMarket) -> City:
    return City(
        name="C",
        local_market=LocalMarket(
            resources_map=generate_resources_for_city_c(),
        ),
        global_market=global_market,
        upgrade_strategy=CityUpgradeStrategy(
            resources_needed={
                ResourceName.Wood: 100,
                ResourceName.Stone: 100
            },
        ),
        production_boost={ResourceName.Gold: Factor(Decimal('1.2'))},
        workshops=generate_workshops_for_city_c()
    )


def generate_city_d(global_market: IGlobalMarket) -> City:
    return City(
        name="D",
        local_market=LocalMarket(
            resources_map=generate_resources_for_city_d(),
        ),
        global_market=global_market,
        upgrade_strategy=CityUpgradeStrategy(
            resources_needed={
                ResourceName.Wood: 100,
                ResourceName.Stone: 100
            },
        ),
        production_boost={ResourceName.Fish: Factor(Decimal('1.2'))},
        workshops=generate_workshops_for_city_d()
    )


def generate_city_e(global_market: IGlobalMarket) -> City:
    return City(
        name="E",
        local_market=LocalMarket(
            resources_map=generate_resources_for_city_e(),
        ),
        global_market=global_market,
        upgrade_strategy=CityUpgradeStrategy(
            resources_needed={
                ResourceName.Wood: 100,
                ResourceName.Stone: 100
            },
        ),
        production_boost={ResourceName.Silk: Factor(Decimal('1.2'))},
        workshops=generate_workshops_for_city_e()
    )
