import unittest
from src.plateau import Plateau
from src.position import Position


class TestPlateau(unittest.TestCase):

    def setUp(self):
        self.plateau = Plateau(5, 5)

    def test_in_bounds(self):
        self.assertTrue(self.plateau.in_bounds(Position(0, 0)))
        self.assertTrue(self.plateau.in_bounds(Position(5, 5)))
        self.assertFalse(self.plateau.in_bounds(Position(6, 5)))
        self.assertFalse(self.plateau.in_bounds(Position(-1, 0)))

    def test_occupy_blocks_place(self):
        pos = Position(1, 2)
        self.assertTrue(self.plateau.can_place(pos))
        self.plateau.occupy(pos)
        self.assertFalse(self.plateau.can_place(pos))

    def test_vacate_frees_cell(self):
        pos = Position(1, 2)
        self.plateau.occupy(pos)
        self.plateau.vacate(pos)
        self.assertTrue(self.plateau.can_place(pos))

    def test_vacate_missing_is_noop(self):
        # Should not raise if the cell was never occupied
        self.plateau.vacate(Position(3, 3))


if __name__ == "__main__":
    unittest.main()