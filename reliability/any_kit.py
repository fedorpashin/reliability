from reliability import Part

from abc import ABC, abstractmethod

from functools import cached_property

__all__ = ['AnyKit']


class AnyKit(ABC):
    def __getitem__(self, key) -> int:
        return self.values[key]

    @property
    @abstractmethod
    def values(self) -> dict[Part, int]:
        pass

    @cached_property
    def n(self) -> int:
        return sum([value for _, value in self.values.items()])
