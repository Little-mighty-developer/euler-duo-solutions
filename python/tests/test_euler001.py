import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.euler001 import sum_multiples_of_3_and_5
import pytest

def test_sum_multiples_of_3_and_5():
    """Test the sum_multiples_of_3_and_5 function with various inputs."""
    # Test case from problem description
    assert sum_multiples_of_3_and_5(10) == 23
    
    # Test with small numbers
    assert sum_multiples_of_3_and_5(1) == 0
    assert sum_multiples_of_3_and_5(3) == 0
    assert sum_multiples_of_3_and_5(4) == 3
    assert sum_multiples_of_3_and_5(6) == 8
    
    # Test with larger numbers
    assert sum_multiples_of_3_and_5(1000) == 233168  # The actual answer to the problem

def test_edge_cases():
    """Test edge cases for the sum_multiples_of_3_and_5 function."""
    # Test with zero
    assert sum_multiples_of_3_and_5(0) == 0
    
    # Test with negative numbers (should handle gracefully)
    with pytest.raises(ValueError):
        sum_multiples_of_3_and_5(-1) 