import sys
import os
import unittest

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..")),
)
from solutions.euler003 import largest_prime_factor  # noqa: E402


class TestEuler003(unittest.TestCase):
    def test_largest_prime_factor(self):
        """Test the largest_prime_factor function with various inputs."""
        # Test case from problem description
        self.assertEqual(largest_prime_factor(13195), 29)
        # Test with small numbers
        self.assertEqual(largest_prime_factor(2), 2)
        self.assertEqual(largest_prime_factor(3), 3)
        self.assertEqual(largest_prime_factor(5), 5)
        self.assertEqual(largest_prime_factor(10), 5)
        self.assertEqual(largest_prime_factor(27), 3)
        self.assertEqual(largest_prime_factor(49), 7)
        # Test with the actual problem number
        self.assertEqual(largest_prime_factor(600851475143), 6857)

    def test_edge_cases(self):
        """Test edge cases for the largest_prime_factor function."""
        # Test with 1 (should raise ValueError)
        with self.assertRaises(ValueError):
            largest_prime_factor(1)
        # Test with 0 (should raise ValueError)
        with self.assertRaises(ValueError):
            largest_prime_factor(0)
        # Test with negative number (should raise ValueError)
        with self.assertRaises(ValueError):
            largest_prime_factor(-10)


if __name__ == "__main__":
    unittest.main()
