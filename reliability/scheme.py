from reliability.part import Part

from dataclasses import dataclass

__all__ = ['Scheme']


@dataclass(frozen=True)
class Scheme:
    __values: dict[Part, tuple[int]]

    def __getitem__(self, key) -> tuple[int]:
        return self.__values[key]

    @property
    def values(self) -> dict[Part, tuple[int]]:
        return self.__values
