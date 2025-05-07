# frozen_string_literal: true

# Project Euler Problem 1: Multiples of 3 or 5
# Find the sum of all the multiples of 3 or 5 below 1000.

def sum_multiples_of_three_and_five(limit)
  raise ArgumentError, 'Limit must be a non-negative integer' if limit.negative?

  (0...limit).select { |n| (n % 3).zero? || (n % 5).zero? }.sum
end

if __FILE__ == $PROGRAM_NAME
  limit = 1000
  result = sum_multiples_of_three_and_five(limit)
  puts "The sum of all multiples of 3 or 5 below #{limit} is: #{result}"
end
