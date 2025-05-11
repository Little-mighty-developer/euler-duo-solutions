import sys
import os
import unittest

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..")),
)
from solutions.euler001 import sum_multiples_of_3_and_5  # noqa: E402


class TestEuler001(unittest.TestCase):
    def test_sum_multiples_of_3_and_5(self):
        """Test the sum_multiples_of_3_and_5 function with various inputs."""
        # Test case from problem description
        self.assertEqual(sum_multiples_of_3_and_5(10), 23)

        # Test with small numbers
        self.assertEqual(sum_multiples_of_3_and_5(1), 0)
        self.assertEqual(sum_multiples_of_3_and_5(3), 0)
        self.assertEqual(sum_multiples_of_3_and_5(4), 3)
        self.assertEqual(sum_multiples_of_3_and_5(6), 8)

        # Test with larger numbers
        self.assertEqual(sum_multiples_of_3_and_5(1000), 233168)

    def test_edge_cases(self):
        """Test edge cases for the sum_multiples_of_3_and_5 function."""
        # Test with zero
        self.assertEqual(sum_multiples_of_3_and_5(0), 0)

        # Test with negative numbers (should handle gracefully)
        with self.assertRaises(ValueError):
            sum_multiples_of_3_and_5(-1)


if __name__ == "__main__":
    unittest.main()
