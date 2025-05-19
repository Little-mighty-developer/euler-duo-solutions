# frozen_string_literal: true

# !/usr/bin/env ruby

require 'test/unit'
require_relative '../euler004'

# Test cases for Project Euler Problem 4: Largest Palindrome Product
class TestEuler004 < Test::Unit::TestCase
  def test_single_digit_palindromes
    assert(palindrome?(1))
    assert(palindrome?(9))
  end

  def test_two_digit_palindromes
    assert(palindrome?(11))
    assert(palindrome?(99))
    assert_false(palindrome?(12))
    assert_false(palindrome?(98))
  end

  def test_three_digit_palindromes
    assert(palindrome?(121))
    assert(palindrome?(999))
    assert_false(palindrome?(123))
    assert_false(palindrome?(998))
  end

  def test_larger_palindromes
    assert(palindrome?(9009))
    assert(palindrome?(12_321))
    assert_false(palindrome?(12_345))
  end

  def test_largest_palindrome_product
    result = largest_palindrome_product
    assert_equal(906_609, result) # The actual answer

    # Verify that the result is a palindrome
    assert(palindrome?(result))

    # Verify that the result is a product of two 3-digit numbers
    factors_found = false
    999.downto(100) do |i|
      next unless (result % i).zero?

      other_factor = result / i
      if other_factor >= 100 && other_factor <= 999
        factors_found = true
        break
      end
    end
    assert(factors_found)
  end
end
