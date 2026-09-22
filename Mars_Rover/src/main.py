from direction import Direction
from position import Position
from plateau import Plateau
from rover import Rover

import sys


def main():

    lines = [l for l in sys.stdin.read().splitlines() if l.strip()]

    if not lines:
        return

    # upper-right coordinates of the plateau
    max_x, max_y = map(int, lines[0].split())

    plateau = Plateau(max_x, max_y)

    i = 1

    while i + 1 < len(lines):
        rov_x, rov_y, rov_dir = lines[i].split()
        commands = lines[i + 1].strip()

        rover = Rover(
            plateau=plateau,
            position=Position(int(rov_x), int(rov_y)),
            direction=Direction[rov_dir],
        )
        rover.execute(commands)

        # prints the final co-ordinates and heading
        print(rover)

        i += 2

    # rov_x, rov_y = int(parts[0]), int(parts[1])
    # rov_dir = parts[2]

    # # String of Commands eg. LMLMLMLMM
    # commands = input("Commands: ")
    # plateau = Plateau(x, y)
    # rover = Rover(plateau=plateau, position=Position(rov_x, rov_y), cur_dir=rov_dir)


if __name__ == "__main__":
    main()
