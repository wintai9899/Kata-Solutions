from position import Position


class Plateau:
    MIN_WIDTH = 0
    MIN_HEIGHT = 0

    def __init__(self, max_width: int, max_height: int):
        self.width: int = max_width
        self.height: int = max_height
        self.occupied: set[Position] = set()

    def in_bounds(self, pos: Position) -> bool:
        return 0 <= pos.x <= self.width and 0 <= pos.y <= self.height

    def is_free(self, pos: Position) -> bool:
        return pos not in self.occupied

    def can_place(self, pos: Position) -> bool:
        return self.in_bounds(pos) and self.is_free(pos)

    def occupy(self, pos: Position) -> None:
        self.occupied.add(pos)

    def vacate(self, pos: Position) -> None:
        self.occupied.discard(pos)
