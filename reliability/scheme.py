from reliability.part import Part

from dataclasses import dataclass

__all__ = ['Scheme']


@dataclass(frozen=True)
class Scheme:
    _values: dict[Part, tuple[int]]

    def __getitem__(self, key):
        return self._values[key]

    @property
    def values(self):
        return self._values
