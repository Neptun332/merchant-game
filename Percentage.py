from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Percentage:
    MAX = 1
    MIN = 0
    value: Decimal

    def __post_init__(self):
        if not 0 <= self.value <= 1:
            raise ValueError(f"When using from_0_1_scale in Percentage value should be from range "
                             f"<0,1>. value={self.value}")
