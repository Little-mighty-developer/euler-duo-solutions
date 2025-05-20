# frozen_string_literal: true

# !/usr/bin/env ruby

require 'test/unit'
require_relative '../euler005'

# Test cases for Project Euler Problem 5: Smallest Multiple
class TestEuler005 < Test::Unit::TestCase
  def test_lcm_small_numbers
    assert_equal(6, lcm(2, 3))
    assert_equal(12, lcm(4, 6))
    assert_equal(24, lcm(8, 12))
  end

  def test_lcm_prime_numbers
    assert_equal(35, lcm(5, 7))
    assert_equal(143, lcm(11, 13))
  end

  def test_lcm_same_numbers
    assert_equal(10, lcm(10, 10))
    assert_equal(15, lcm(15, 15))
  end

  def test_lcm_multiple_relationship
    assert_equal(8, lcm(4, 8))
    assert_equal(18, lcm(6, 18))
  end

  def test_smallest_multiple
    # Test with the example from the problem description
    assert_equal(2520, smallest_multiple(10))

    # Test with small ranges
    assert_equal(1, smallest_multiple(1))
    assert_equal(2, smallest_multiple(2))
    assert_equal(6, smallest_multiple(3))
    assert_equal(12, smallest_multiple(4))
    assert_equal(60, smallest_multiple(5))

    # Test with the actual problem
    assert_equal(232_792_560, smallest_multiple(20))
  end
end
