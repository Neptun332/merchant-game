from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Factor:
    value: Decimal
