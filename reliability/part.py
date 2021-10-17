from dataclasses import dataclass

__all__ = ['Part']


@dataclass(frozen=True)
class Part:
    type_: int
    λ: float
