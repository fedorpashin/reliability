from dataclasses import dataclass

from functools import cached_property

__all__ = ['Part',
           'Kit']


@dataclass(frozen=True)
class Part:
    type_: int
    λ: float


@dataclass(frozen=True)
class Kit:
    _values: dict[Part, int]

    def __getitem__(self, key):
        return self._values[key]

    @property
    def values(self):
        return self._values

    @cached_property
    def n(self):
        return sum([value for _, value in self._values.items()])
