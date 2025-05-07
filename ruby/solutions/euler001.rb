# Project Euler Problem 1: Multiples of 3 or 5
# Find the sum of all the multiples of 3 or 5 below 1000.

def sum_multiples_of_3_and_5(limit)
  raise ArgumentError, "Limit must be a non-negative integer" if limit < 0
  (0...limit).select { |n| n % 3 == 0 || n % 5 == 0 }.sum
end

if __FILE__ == $0
  limit = 1000
  result = sum_multiples_of_3_and_5(limit)
  puts "The sum of all multiples of 3 or 5 below #{limit} is: #{result}"
end 