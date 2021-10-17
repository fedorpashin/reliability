from abc import ABC, abstractmethod

from functools import cached_property

__all__ = ['AnyKit']


class AnyKit(ABC):
    def __getitem__(self, key):
        return self.values[key]

    @property
    @abstractmethod
    def values(self):
        pass

    @cached_property
    def n(self):
        return sum([value for _, value in self.values.items()])
