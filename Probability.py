from dataclasses import dataclass


@dataclass(frozen=True)
class Probability:
    MAX = 1
    MIN = 0
    value: float

    def __post_init__(self):
        if not 0 <= self.value <= 1:
            raise ValueError(f"When using from_0_1_scale in Probability value should be from range "
                             f"<0,1>. value={self.value}")

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value
