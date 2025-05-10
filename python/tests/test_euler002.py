import sys
import os
import unittest

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..")),
)
from solutions.euler002 import sum_even_fibonacci  # noqa: E402


class TestEuler002(unittest.TestCase):
    def test_sum_even_fibonacci(self):
        """Test the sum_even_fibonacci function with various inputs."""
        # Test with small numbers
        self.assertEqual(sum_even_fibonacci(10), 10)  # 2 + 8 = 10
        self.assertEqual(sum_even_fibonacci(20), 10)  # 2 + 8 = 10
        self.assertEqual(sum_even_fibonacci(50), 44)  # 2 + 8 + 34 = 44

        # Test with the actual problem limit
        self.assertEqual(sum_even_fibonacci(4_000_000), 4613732)

    def test_edge_cases(self):
        """Test edge cases for the sum_even_fibonacci function."""
        # Test with zero
        self.assertEqual(sum_even_fibonacci(0), 0)

        # Test with one
        self.assertEqual(sum_even_fibonacci(1), 0)

        # Test with two
        self.assertEqual(sum_even_fibonacci(2), 0)

        # Test with negative numbers (should handle gracefully)
        with self.assertRaises(ValueError):
            sum_even_fibonacci(-1)


if __name__ == "__main__":
    unittest.main()
