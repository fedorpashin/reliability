from .parts import Part, Kit

from typing import Optional, Protocol
from dataclasses import dataclass

from numpy import random
import scipy.stats
import itertools

from functools import cached_property

import numpy as np

__all__ = ['Scheme',
           'System']


@dataclass(frozen=True)
class Scheme:
    _values: dict[Part, tuple[int]]

    def __getitem__(self, key):
        return self._values[key]

    @property
    def values(self):
        return self._values


class StructureFunction(Protocol):
    def __call__(self, __origin: tuple[bool, ...]) -> bool: ...


class System:
    _parts: tuple[Part, ...]
    _scheme: Scheme
    __is_working: StructureFunction

    def __init__(self, parts: tuple[Part, ...], scheme: Scheme, structure_function: StructureFunction):
        """
        :param parts: types of parts
        :param scheme: allocation of parts in scheme
        :param structure_function: structure function
        """
        self._parts = parts
        self._scheme = scheme
        self.__is_working = structure_function

    @property
    def parts(self):
        return self._parts

    @property
    def scheme(self):
        return self._scheme

    @cached_property
    def n(self):
        return sum([len(self._scheme[part]) for part in self._parts])

    def reliability_for(self, kit: Kit, T: int, α: float) -> float:
        """
        :param kit: kit for simulation
        :param T: simulation time
        :param α: accuracy
        :return: probability of survival
        """
        assert 0 <= α <= 1
        assert T > 0
        ε = 1 - α
        N = round(scipy.stats.norm.ppf(α)**2 * ε * α / ε**2)
        d = 0
        for _ in range(N):
            t: list[float] = list(np.zeros(self.n))
            for part in self._parts:
                part_t = [random.exponential(1 / part.λ) for _ in self._scheme[part]]
                for position in range(kit[part]):
                    part_t[part_t.index(min(part_t))] += random.exponential(1 / part.λ)
                for i, position in enumerate(self._scheme[part]):
                    t[position] = part_t[i]
            if not self.__is_working(tuple(t_i > T for t_i in t)):
                d += 1
        return 1 - d / N

    def possible_kits_for(self, P0: float, T: int, α: float, threshold: dict[Part, int]) -> list[Kit]:
        """
        :param P0: required probability
        :param T: simulation time
        :param α: accuracy
        :param threshold: threshold quantity for simulation
        :return: list of kits
        """
        assert 0 <= P0 <= 1
        result = []
        list_of_tuples = itertools.product(*([range(1, threshold[part] + 1) for part in self._parts]))
        list_of_kits = [Kit({part: L[i] for i, part in enumerate(self._parts)}) for L in list_of_tuples]
        for kit in list_of_kits:
            if self.reliability_for(kit, T, α) > P0:
                result.append(kit)
        return result

    def min_possible_kit_for(self, P0: float, T: int, α: float, threshold: dict[Part, int]) -> Optional[Kit]:
        """
        :param P0: required probability
        :param T: simulation time
        :param α: accuracy
        :param threshold: threshold quantity for simulation
        :return: kit if there is one, None otherwise
        """
        kits = self.possible_kits_for(P0, T, α, threshold)
        if not kits:
            return None
        else:
            return min(kits, key=lambda x: x.n)
