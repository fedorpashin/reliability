from abc import ABC, abstractmethod

__all__ = ['Kits']


class Kits(ABC):
    @property
    @abstractmethod
    def all(self):
        pass
