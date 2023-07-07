from decimal import Decimal

from Factor import Factor
from event_engine.TheftEvent import TheftEvent


class PercentageTheftEvent(TheftEvent):
    DEFAULT_UNITS_PERCENTAGE = Factor(Decimal(0.5))

    def _calculate_units_count(self) -> int:
        return int(self.city.local_market.get_resource_units(self.random_resource_name) * self.DEFAULT_UNITS_PERCENTAGE.value)

    def _re_register_event(self):
        self.event_engine.register_possible_event([PercentageTheftEvent(self.city, self.event_config, self.event_engine)])
