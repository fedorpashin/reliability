import itertools

from reliability.kits import Kits
from reliability.system import System
from reliability.part import Part
from reliability.any_kit import AnyKit
from reliability.kit import Kit
from reliability.reliability import Reliability

from dataclasses import dataclass
from typing import Iterable
from final_class import final
from overrides import overrides

__all__ = ['SuitableKits']


@final
@dataclass(frozen=True)
class SuitableKits(Kits):
    """
    A class used to represent list of suitable kits

    Attributes
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

    @overrides
    def all(self) -> Iterable[AnyKit]:
        assert 0 <= self.P0 <= 1
        result = []
        list_of_tuples = itertools.product(*([range(1, self.threshold[part] + 1) for part in self.system.parts]))
        list_of_kits = [Kit({part: L[i] for i, part in enumerate(self.system.parts)}) for L in list_of_tuples]
        for kit in list_of_kits:
            if Reliability(self.system, kit, self.T, self.α) > self.P0:
                result.append(kit)
        return result
