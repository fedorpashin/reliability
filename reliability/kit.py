from reliability.any_kit import AnyKit
from reliability.part import Part

from dataclasses import dataclass

__all__ = ['Kit']


@dataclass(frozen=True)
class Kit(AnyKit):
    __values: dict[Part, int]

    @property
    def values(self):
        return self.__values
