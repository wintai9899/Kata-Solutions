from dataclasses import dataclass


@dataclass(frozen=True)
class Position:

    x: int = 0
    y: int = 0
