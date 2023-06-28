from city.CityUpgradeStrategy import CityUpgradeStrategy
from market.ResourceName import ResourceName


def generate_upgrade_strategy_for_city_a() -> CityUpgradeStrategy:
    return CityUpgradeStrategy(
        resources_needed={
            ResourceName.Wood: 100,
            ResourceName.Stone: 100
        },
    )
