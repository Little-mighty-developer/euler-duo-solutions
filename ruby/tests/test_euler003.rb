# frozen_string_literal: true

require 'minitest/autorun'
require_relative '../solutions/euler003'

# Test cases for Project Euler Problem 3
class TestEuler003 < Minitest::Test
  def test_largest_prime_factor
    # Test case from problem description
    assert_equal 29, Euler::Euler003.largest_prime_factor(13_195)

    # Test with small numbers
    assert_equal 2, Euler::Euler003.largest_prime_factor(2)
    assert_equal 3, Euler::Euler003.largest_prime_factor(3)
    assert_equal 5, Euler::Euler003.largest_prime_factor(5)
    assert_equal 5, Euler::Euler003.largest_prime_factor(10)
    assert_equal 3, Euler::Euler003.largest_prime_factor(27)
    assert_equal 7, Euler::Euler003.largest_prime_factor(49)

    # Test with the actual problem number
    assert_equal 6857, Euler::Euler003.largest_prime_factor(600_851_475_143)
  end

  def test_edge_cases
    # Test with 1 (should raise ArgumentError)
    assert_raises(ArgumentError) do
      Euler::Euler003.largest_prime_factor(1)
    end

    # Test with 0 (should raise ArgumentError)
    assert_raises(ArgumentError) do
      Euler::Euler003.largest_prime_factor(0)
    end

    # Test with negative number (should raise ArgumentError)
    assert_raises(ArgumentError) do
      Euler::Euler003.largest_prime_factor(-10)
    end
  end
end
