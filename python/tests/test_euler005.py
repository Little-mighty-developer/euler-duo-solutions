import sys
import os
import unittest

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..")),
)
from solutions.euler005 import lcm, smallest_multiple  # noqa: E402


class TestEuler005(unittest.TestCase):
    def test_lcm(self):
        """Test the lcm function with various inputs."""
        # Test with small numbers
        self.assertEqual(lcm(2, 3), 6)
        self.assertEqual(lcm(4, 6), 12)
        self.assertEqual(lcm(8, 12), 24)

        # Test with prime numbers
        self.assertEqual(lcm(5, 7), 35)
        self.assertEqual(lcm(11, 13), 143)

        # Test with same numbers
        self.assertEqual(lcm(10, 10), 10)
        self.assertEqual(lcm(15, 15), 15)

        # Test with one number being a multiple of the other
        self.assertEqual(lcm(4, 8), 8)
        self.assertEqual(lcm(6, 18), 18)

    def test_smallest_multiple(self):
        """Test the smallest_multiple function."""
        # Test with the example from the problem description
        self.assertEqual(smallest_multiple(10), 2520)

        # Test with small ranges
        self.assertEqual(smallest_multiple(1), 1)
        self.assertEqual(smallest_multiple(2), 2)
        self.assertEqual(smallest_multiple(3), 6)
        self.assertEqual(smallest_multiple(4), 12)
        self.assertEqual(smallest_multiple(5), 60)

        # Test with the actual problem
        self.assertEqual(smallest_multiple(20), 232_792_560)


if __name__ == "__main__":
    unittest.main()
