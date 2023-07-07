from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Factor:
    DEFAULT = Decimal(1)
    value: Decimal

    @classmethod
    def from_default(cls) -> 'Factor':
        return cls(value=cls.DEFAULT)
