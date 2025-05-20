"""
Test cases for Project Euler Problem 6: Sum Square Difference
"""

import unittest
from solutions.euler006 import sum_square_difference


class TestEuler006(unittest.TestCase):
    def test_small_numbers(self):
        """Test with small numbers from the problem description."""
        self.assertEqual(2640, sum_square_difference(10))

    def test_single_number(self):
        """Test with a single number."""
        self.assertEqual(0, sum_square_difference(1))

    def test_two_numbers(self):
        """Test with two numbers."""
        # (1 + 2)² - (1² + 2²) = 9 - 5 = 4
        self.assertEqual(4, sum_square_difference(2))

    def test_three_numbers(self):
        """Test with three numbers."""
        # (1 + 2 + 3)² - (1² + 2² + 3²) = 36 - 14 = 22
        self.assertEqual(22, sum_square_difference(3))

    def test_large_number(self):
        """Test with the actual problem input."""
        self.assertEqual(25_164_150, sum_square_difference(100))


if __name__ == "__main__":
    unittest.main()
