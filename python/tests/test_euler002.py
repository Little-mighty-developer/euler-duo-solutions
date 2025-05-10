import sys
import os
import pytest

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..")),
)
from solutions.euler002 import sum_even_fibonacci  # noqa: E402


def test_sum_even_fibonacci():
    """Test the sum_even_fibonacci function with various inputs."""
    # Test with small numbers
    assert sum_even_fibonacci(10) == 10  # 2 + 8 = 10
    assert sum_even_fibonacci(20) == 10  # 2 + 8 = 10
    assert sum_even_fibonacci(50) == 44  # 2 + 8 + 34 = 44

    # Test with the actual problem limit
    assert sum_even_fibonacci(4_000_000) == 4613732


def test_edge_cases():
    """Test edge cases for the sum_even_fibonacci function."""
    # Test with zero
    assert sum_even_fibonacci(0) == 0

    # Test with one
    assert sum_even_fibonacci(1) == 0

    # Test with two
    assert sum_even_fibonacci(2) == 0

    # Test with negative numbers (should handle gracefully)
    with pytest.raises(ValueError):
        sum_even_fibonacci(-1)
