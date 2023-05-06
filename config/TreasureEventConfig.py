from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class TreasureEventConfig:
    _MAX_GOLD_RANGE_PARAMS = 2
    gold_range: Tuple[int, int]

    def __post_init__(self):
        if len(self.gold_range) != self._MAX_GOLD_RANGE_PARAMS:
            raise ValueError(f"Gold range should have exactly 2 values. value={self.gold_range}")
        if self.gold_range[0] > self.gold_range[1]:
            raise ValueError(f"Gold range Second value should be greater than first one. value={self.gold_range}")
