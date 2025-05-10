# frozen_string_literal: true

require 'simplecov'
SimpleCov.start

require 'minitest/autorun'
require_relative '../solutions/euler002'

# Tests for the sum_even_fibonacci method from Project Euler Problem 2.
class TestEuler002 < Minitest::Test
  def test_sum_even_fibonacci
    # Test with small numbers
    assert_equal 10, sum_even_fibonacci(10)  # 2 + 8 = 10
    assert_equal 10, sum_even_fibonacci(20)  # 2 + 8 = 10
    assert_equal 10, sum_even_fibonacci(21)  # 2 + 8 = 10 (21 is not included)
    assert_equal 44, sum_even_fibonacci(50)  # 2 + 8 + 34 = 44

    # Test with the actual problem limit
    assert_equal 4_613_732, sum_even_fibonacci(4_000_000)
  end

  def test_edge_cases
    # Test with zero
    assert_equal 0, sum_even_fibonacci(0)

    # Test with one
    assert_equal 0, sum_even_fibonacci(1)

    # Test with two
    assert_equal 0, sum_even_fibonacci(2)

    # Test with negative numbers (should handle gracefully)
    assert_raises(ArgumentError) { sum_even_fibonacci(-1) }
  end
end
