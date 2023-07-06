from dataclasses import dataclass
from typing import Tuple

from Probability import Probability


@dataclass(frozen=True)
class BaseEventConfig:
    _MAX_UNITS_RANGE_PARAMS = 2
    units_count_range: Tuple[int, int]
    probability: Probability

    def __post_init__(self):
        if len(self.units_count_range) != self._MAX_UNITS_RANGE_PARAMS:
            raise ValueError(f"Units count range should have exactly 2 values. value={self.units_count_range}")
        if self.units_count_range[0] > self.units_count_range[1]:
            raise ValueError(f"Units count range second value should be greater than first one. "
                             f"value={self.units_count_range}")
