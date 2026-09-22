import unittest
from src.direction import Direction


class TestDirection(unittest.TestCase):

    def test_left_cycles_counter_clockwise(self):
        self.assertIs(Direction.N.turn_left(), Direction.W)
        self.assertIs(Direction.W.turn_left(), Direction.S)
        self.assertIs(Direction.S.turn_left(), Direction.E)
        self.assertIs(Direction.E.turn_left(), Direction.N)

    def test_turn_right_cycles_clockwise(self):
        self.assertIs(Direction.N.turn_left(), Direction.W)
        self.assertIs(Direction.W.turn_left(), Direction.S)
        self.assertIs(Direction.S.turn_left(), Direction.E)
        self.assertIs(Direction.E.turn_left(), Direction.N)

    def test_delta_returns_unit_step(self):
        self.assertEqual(Direction.N.delta == (0, 1))
        self.assertEqual(Direction.N.delta(), (0, 1))
        self.assertEqual(Direction.E.delta(), (1, 0))
        self.assertEqual(Direction.S.delta(), (0, -1))
        self.assertEqual(Direction.W.delta(), (-1, 0))

if __name__ == "__main__":
    unittest.main()