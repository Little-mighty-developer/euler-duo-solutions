"""
Project Euler Problem 3: Largest Prime Factor

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""


def largest_prime_factor(n: int) -> int:
    """
    Find the largest prime factor of a given number n.

    Args:
        n (int): The number to factorize

    Returns:
        int: The largest prime factor of n

    Raises:
        ValueError: If n is less than 2
    """
    if n < 2:
        raise ValueError("Input must be greater than 1")
    factor = 2
    last_factor = 1
    while n > 1:
        if n % factor == 0:
            last_factor = factor
            n //= factor
            while n % factor == 0:
                n //= factor
        factor += 1
        if factor * factor > n and n > 1:
            last_factor = n
            break
    return last_factor


def main():
    """Main function to solve and display the answer."""
    number = 600851475143
    result = largest_prime_factor(number)
    print(f"The largest prime factor of {number} is: {result}")


if __name__ == "__main__":
    main()
