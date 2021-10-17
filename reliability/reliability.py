from reliability.system import System
from reliability.kit import Kit

from final_class import final

import numpy as np
from numpy import random
import scipy.stats  # type: ignore

__all__ = ['Reliability']


@final
class Reliability(float):
    """
    A class used to represent the probability of system survival

    Attributes
    system: target system
    kit: kit for simulation
    T: simulation time
    α: accuracy
    """

    __system: System
    __kit: Kit
    __T: int
    __α: float

    def __new__(cls, system: System, kit: Kit, T: int, α: float) -> 'Reliability':
        return super().__new__(cls, cls.__value(system, kit, T, α))

    def __init__(self, system: System, kit: Kit, T: int, α: float):
        self.__system = system
        self.__kit = kit
        self.__T = T
        self.__α = α

    @staticmethod
    def __value(system: System, kit: Kit, T: int, α: float):
        assert 0 <= α <= 1
        assert T > 0
        ε = 1 - α
        N = round(scipy.stats.norm.ppf(α)**2 * ε * α / ε**2)
        d = 0
        for _ in range(N):
            t: list[float] = list(np.zeros(system.n))
            for part in system.parts:
                part_t = [random.exponential(1 / part.λ) for _ in system.scheme[part]]
                for position in range(kit[part]):
                    part_t[part_t.index(min(part_t))] += random.exponential(1 / part.λ)
                for i, position in enumerate(system.scheme[part]):
                    t[position] = part_t[i]
            if not system.is_working(tuple(t_i > T for t_i in t)):
                d += 1
        return 1 - d / N

    @property
    def system(self):
        return self.system

    @property
    def kit(self):
        return self.kit

    @property
    def T(self):
        return self.T

    @property
    def α(self):
        return self.α
