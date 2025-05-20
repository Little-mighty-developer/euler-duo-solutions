# frozen_string_literal: true

# !/usr/bin/env ruby

# Project Euler Problem 5: Smallest Multiple
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10
# without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers
# from 1 to 20?

def gcd(first_num, second_num)
  second_num.zero? ? first_num : gcd(second_num, first_num % second_num)
end

def lcm(first_num, second_num)
  (first_num * second_num).abs / gcd(first_num, second_num)
end

def smallest_multiple(max_num)
  (2..max_num).reduce(1) { |result, i| lcm(result, i) }
end

puts smallest_multiple(20) if __FILE__ == $PROGRAM_NAME
