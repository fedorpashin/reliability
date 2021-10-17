from reliability.part import Part

from dataclasses import dataclass

from functools import cached_property

__all__ = ['Kit']


@dataclass(frozen=True)
class Kit:
    __values: dict[Part, int]

    def __getitem__(self, key):
        return self.__values[key]

    @property
    def values(self):
        return self.__values

    @cached_property
    def n(self):
        return sum([value for _, value in self.__values.items()])
