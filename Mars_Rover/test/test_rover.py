import unittest
from src.plateau import Plateau
from src.position import Position
from src.direction import Direction
from src.rover import Rover


class TestRover(unittest.TestCase):

    def test_sample_rover_1(self):
        plateau = Plateau(5, 5)
        rover = Rover(plateau, Position(1, 2), Direction.N)
        rover.execute("LMLMLMLMM")
        self.assertEqual(str(rover), "1 3 N")

    def test_sample_rover_2(self):
        plateau = Plateau(5, 5)
        Rover(plateau, Position(1, 2), Direction.N)          # occupy (1,2)
        rover = Rover(plateau, Position(3, 3), Direction.E)
        rover.execute("MMRMMRMRRM")
        self.assertEqual(str(rover), "5 1 E")

    def test_blocked_by_grid_edge(self):
        plateau = Plateau(5, 5)
        rover = Rover(plateau, Position(5, 5), Direction.N)
        rover.execute("M")
        self.assertEqual(rover.position, Position(5, 5))

    def test_blocked_by_other_rover(self):
        plateau = Plateau(5, 5)
        Rover(plateau, Position(1, 3), Direction.N)          # blocks (1,3)
        rover = Rover(plateau, Position(1, 2), Direction.N)
        rover.execute("M")
        self.assertEqual(rover.position, Position(1, 2))

    def test_cannot_deploy_on_occupied(self):
        plateau = Plateau(5, 5)
        Rover(plateau, Position(1, 2), Direction.N)
        with self.assertRaises(ValueError):
            Rover(plateau, Position(1, 2), Direction.N)

    def test_invalid_command_raises(self):
        plateau = Plateau(5, 5)
        rover = Rover(plateau, Position(0, 0), Direction.N)
        with self.assertRaises(ValueError):
            rover.execute("X")


if __name__ == "__main__":
    unittest.main()