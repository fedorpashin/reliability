from reliability.any_kit import AnyKit
from reliability.part import Part

from dataclasses import dataclass
from final_class import final

__all__ = ['Kit']


@final
@dataclass(frozen=True)
class Kit(AnyKit):
    __values: dict[Part, int]

    @property
    def values(self) -> dict[Part, int]:
        return self.__values
