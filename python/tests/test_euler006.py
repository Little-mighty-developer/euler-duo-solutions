"""
Test cases for Project Euler Problem 6: Sum Square Difference
"""

import unittest
from solutions.euler006 import sum_square_difference


class TestEuler006(unittest.TestCase):
    def test_sum_square_difference(self):
        """Test the sum_square_difference function with known values."""
        # Test case from problem description
        self.assertEqual(sum_square_difference(10), 2640)

        # Test with n = 1
        self.assertEqual(sum_square_difference(1), 0)

        # Test with n = 2
        self.assertEqual(sum_square_difference(2), 4)

        # Test with n = 3
        self.assertEqual(sum_square_difference(3), 22)

        # Test with n = 4
        self.assertEqual(sum_square_difference(4), 70)

        # Test with n = 5
        self.assertEqual(sum_square_difference(5), 170)


if __name__ == "__main__":
    unittest.main()
