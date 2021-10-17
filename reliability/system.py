from reliability.scheme import Scheme
from reliability.part import Part

from dataclasses import dataclass
from typing import Protocol

from functools import cached_property

__all__ = ['System']


class StructureFunction(Protocol):
    def __call__(self, __origin: tuple[bool, ...]) -> bool: ...  # noqa: E704


@dataclass(frozen=True)
class System:
    parts: tuple[Part, ...]
    scheme: Scheme
    structure_function: StructureFunction

    def is_working(self, __origin: tuple[bool, ...]) -> bool:
        return self.structure_function(__origin)

    @cached_property
    def n(self) -> int:
        return sum([len(self.scheme[part]) for part in self.parts])
