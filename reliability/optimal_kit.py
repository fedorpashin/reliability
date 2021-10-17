from reliability.system import System
from reliability.part import Part
from reliability.suitable_kits import SuitableKits

from dataclasses import dataclass
from typing import Optional

from functools import cached_property

__all__ = ['OptimalKit']


@dataclass(frozen=True)
class OptimalKit:
    """
    A class used to represent optimal kit if there is one, None otherwise

    Attributes
    system: target system
    P0: required probability
    T: simulation time
    α: accuracy
    threshold: threshold quantity for simulation
    """

    system: System
    P0: float
    T: int
    α: float
    threshold: dict[Part, int]

    @cached_property
    def value(self) -> Optional[dict[Part, int]]:
        kits = SuitableKits(self.system, self.P0, self.T, self.α, self.threshold).all()
        return min(kits, key=lambda x: x.n) if kits else None
