from dataclasses import dataclass

from final_class import final

__all__ = ['Part']


@final
@dataclass(frozen=True)
class Part:
    type_: int
    λ: float
