# frozen_string_literal: true

require 'test/unit'
require_relative '../euler006'

# Test cases for Project Euler Problem 6: Sum Square Difference
class TestEuler006 < Test::Unit::TestCase
  def test_sum_square_difference
    # Test case from problem description
    assert_equal(2640, sum_square_difference(10))

    # Test with n = 1
    assert_equal(0, sum_square_difference(1))

    # Test with n = 2
    assert_equal(4, sum_square_difference(2))

    # Test with n = 3
    assert_equal(22, sum_square_difference(3))

    # Test with n = 4
    assert_equal(70, sum_square_difference(4))

    # Test with n = 5
    assert_equal(170, sum_square_difference(5))
  end
end
