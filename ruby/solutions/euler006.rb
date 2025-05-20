# frozen_string_literal: true

# !/usr/bin/env ruby

# Project Euler Problem 6: Sum Square Difference
#
# The sum of the squares of the first ten natural numbers is:
# 1² + 2² + ... + 10² = 385
#
# The square of the sum of the first ten natural numbers is:
# (1 + 2 + ... + 10)² = 55² = 3025
#
# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025 - 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

def sum_square_difference(number)
  # Sum of squares: 1² + 2² + ... + n²
  sum_of_squares = (1..number).sum { |i| i * i }

  # Square of sum: (1 + 2 + ... + n)²
  square_of_sum = (1..number).sum**2

  square_of_sum - sum_of_squares
end

puts sum_square_difference(100) if __FILE__ == $PROGRAM_NAME
