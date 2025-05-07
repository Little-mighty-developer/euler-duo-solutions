require 'minitest/autorun'
require_relative '../solutions/euler001'

class TestEuler001 < Minitest::Test
  def test_sum_multiples_of_3_and_5
    assert_equal 23, sum_multiples_of_3_and_5(10)
    assert_equal 0, sum_multiples_of_3_and_5(1)
    assert_equal 0, sum_multiples_of_3_and_5(3)
    assert_equal 3, sum_multiples_of_3_and_5(4)
    assert_equal 8, sum_multiples_of_3_and_5(6)
    assert_equal 233168, sum_multiples_of_3_and_5(1000)
  end

  def test_edge_cases
    assert_equal 0, sum_multiples_of_3_and_5(0)
    assert_raises(ArgumentError) { sum_multiples_of_3_and_5(-1) }
  end
end 