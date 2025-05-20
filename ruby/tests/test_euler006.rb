# frozen_string_literal: true

# !/usr/bin/env ruby

require 'test/unit'
require_relative '../solutions/euler006'

# Test cases for Project Euler Problem 6: Sum Square Difference
class TestEuler006 < Test::Unit::TestCase
  def test_small_numbers
    # Test with small numbers from the problem description
    assert_equal(2640, sum_square_difference(10))
  end

  def test_single_number
    # Test with a single number
    assert_equal(0, sum_square_difference(1))
  end

  def test_two_numbers
    # Test with two numbers
    # (1 + 2)² - (1² + 2²) = 9 - 5 = 4
    assert_equal(4, sum_square_difference(2))
  end

  def test_three_numbers
    # Test with three numbers
    # (1 + 2 + 3)² - (1² + 2² + 3²) = 36 - 14 = 22
    assert_equal(22, sum_square_difference(3))
  end

  def test_large_number
    # Test with the actual problem input
    assert_equal(25_164_150, sum_square_difference(100))
  end
end
