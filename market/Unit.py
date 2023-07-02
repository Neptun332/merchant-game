from dataclasses import dataclass
from typing import Optional

from city.ICity import ICity


@dataclass
class Unit:
    DEFAULT_UNIT_LIFE_TIME = 180
    ttl: int  # ticks to live
    produced_by: Optional[ICity]

    def set_produced_by(self, produced_by: ICity):
        self.produced_by = produced_by

    def get_ttl(self) -> int:
        return self.ttl
