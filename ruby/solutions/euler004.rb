# frozen_string_literal: true

# !/usr/bin/env ruby

# Project Euler Problem 4: Largest Palindrome Product
#
# A palindromic number reads the same both ways. The largest palindrome made from
# the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def palindrome?(number)
  number.to_s == number.to_s.reverse
end

def largest_palindrome_product
  largest_palindrome = 0
  999.downto(100) do |i|
    i.downto(100) do |j|
      product = i * j
      break if product < largest_palindrome

      largest_palindrome = product if palindrome?(product)
    end
  end
  largest_palindrome
end

puts largest_palindrome_product if __FILE__ == $PROGRAM_NAME
