from reliability.any_kit import AnyKit

from abc import ABC, abstractmethod
from typing import Iterable

__all__ = ['Kits']


class Kits(ABC):
    @property
    @abstractmethod
    def all(self) -> Iterable[AnyKit]:
        pass
