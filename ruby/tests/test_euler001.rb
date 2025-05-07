# frozen_string_literal: true

require 'simplecov'
SimpleCov.start

require 'minitest/autorun'
require_relative '../solutions/euler001'

#  Tests for the sum_multiples_of_three_and_five method from Project Euler Problem 1.
class TestEuler001 < Minitest::Test
  def test_sum_multiples_of_three_and_five
    assert_equal 23, sum_multiples_of_three_and_five(10)
    assert_equal 0, sum_multiples_of_three_and_five(1)
    assert_equal 0, sum_multiples_of_three_and_five(3)
    assert_equal 3, sum_multiples_of_three_and_five(4)
    assert_equal 8, sum_multiples_of_three_and_five(6)
    assert_equal 233_168, sum_multiples_of_three_and_five(1000)
  end

  def test_edge_cases
    assert_equal 0, sum_multiples_of_three_and_five(0)
    assert_raises(ArgumentError) { sum_multiples_of_three_and_five(-1) }
  end
end
