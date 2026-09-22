from plateau import Plateau
from position import Position
from direction import Direction


class Rover:

    def __init__(self, plateau: Plateau, position: Position, direction: Direction):
        self.plateau: Plateau = plateau
        self.position: Position = position

        if not self.plateau.can_place(position):
            raise ValueError(f"Cannot deploy rover at position: {position}")

        self.plateau.occupy(position)
        self.direction = direction

    def __repr__(self):
        return f"{self.position.x} {self.position.y} {self.direction.name}"

    def turn_left(self) -> None:
        self.direction = self.direction.turn_left()

    def turn_right(self) -> None:
        self.direction = self.direction.turn_right()

    def move(self) -> None:
        dx, dy = self.direction.delta()
        new_pos = Position(self.position.x + dx, self.position.y + dy)

        if not self.plateau.can_place(new_pos):
            return

        self.plateau.vacate(self.position)
        self.plateau.occupy(new_pos)
        self.position = new_pos

    def execute(self, commands: str) -> None:
        for command in commands:
            if command == "L":
                self.turn_left()

            elif command == "R":
                self.turn_right()

            elif command == "M":
                self.move()

            else:
                raise ValueError(f"Not Valid Command: {command}")
