# frozen_string_literal: true

# Project Euler Problem 3: Largest Prime Factor
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

module Euler
  # Solution for Project Euler Problem 3
  class Euler003
    # Find the largest prime factor of a given number
    #
    # @param number [Integer] the number to factorize
    # @return [Integer] the largest prime factor
    # @raise [ArgumentError] if number is less than 2
    def self.largest_prime_factor(number)
      raise ArgumentError, 'Input must be greater than 1' if number < 2

      factor = 2
      last_factor = 1
      remaining = number

      while remaining > 1
        last_factor = process_factor(remaining, factor, last_factor)
        remaining = remove_factor(remaining, factor)
        break if should_break?(remaining, factor)

        factor += 1
      end
      last_factor
    end

    # Process a single factor
    #
    # @param remaining [Integer] remaining number to factorize
    # @param factor [Integer] current factor to check
    # @param last_factor [Integer] last found factor
    # @return [Integer] updated last factor
    def self.process_factor(remaining, factor, last_factor)
      return last_factor unless (remaining % factor).zero?

      factor
    end

    # Remove all instances of a factor from the number
    #
    # @param number [Integer] number to process
    # @param factor [Integer] factor to remove
    # @return [Integer] number after removing factor
    def self.remove_factor(number, factor)
      return number unless (number % factor).zero?

      result = number / factor
      result = remove_factor(result, factor) while (result % factor).zero?
      result
    end

    # Check if we should break the main loop
    #
    # @param remaining [Integer] remaining number
    # @param factor [Integer] current factor
    # @return [Boolean] true if we should break
    def self.should_break?(remaining, factor)
      factor * factor > remaining && remaining > 1
    end

    def self.main
      number = 600_851_475_143
      result = largest_prime_factor(number)
      puts "The largest prime factor of #{number} is: #{result}"
    end
  end
end

Euler::Euler003.main if __FILE__ == $PROGRAM_NAME
