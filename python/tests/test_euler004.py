import sys
import os
import unittest

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..")),
)
from solutions.euler004 import (  # noqa: E402
    is_palindrome,
    largest_palindrome_product,
)


class TestEuler004(unittest.TestCase):
    def test_is_palindrome(self):
        """Test the is_palindrome function with various inputs."""
        # Test single digit numbers
        self.assertTrue(is_palindrome(1))
        self.assertTrue(is_palindrome(9))

        # Test two digit numbers
        self.assertTrue(is_palindrome(11))
        self.assertTrue(is_palindrome(99))
        self.assertFalse(is_palindrome(12))
        self.assertFalse(is_palindrome(98))

        # Test three digit numbers
        self.assertTrue(is_palindrome(121))
        self.assertTrue(is_palindrome(999))
        self.assertFalse(is_palindrome(123))
        self.assertFalse(is_palindrome(998))

        # Test larger numbers
        self.assertTrue(is_palindrome(9009))
        self.assertTrue(is_palindrome(12321))
        self.assertFalse(is_palindrome(12345))

    def test_largest_palindrome_product(self):
        """Test the largest_palindrome_product function."""
        result = largest_palindrome_product()
        self.assertEqual(result, 906609)  # The actual answer

        # Verify that the result is a palindrome
        self.assertTrue(is_palindrome(result))

        # Verify that the result is a product of two 3-digit numbers
        factors_found = False
        for i in range(999, 99, -1):
            if result % i == 0:
                other_factor = result // i
                if 100 <= other_factor <= 999:
                    factors_found = True
                    break
        self.assertTrue(factors_found)


if __name__ == "__main__":
    unittest.main()
