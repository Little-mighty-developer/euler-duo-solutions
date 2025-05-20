"""
Project Euler Problem 5: Smallest Multiple

2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""

import math


def lcm(a: int, b: int) -> int:
    """
    Calculate the Least Common Multiple (LCM) of two numbers.

    Args:
        a: First number
        b: Second number

    Returns:
        int: The LCM of a and b
    """
    return abs(a * b) // math.gcd(a, b)


def smallest_multiple(n: int) -> int:
    """
    Find the smallest positive number that is evenly divisible by all numbers
    from 1 to n.

    Args:
        n: Upper bound of the range (inclusive)

    Returns:
        int: The smallest positive number evenly divisible by all numbers from
        1 to n
    """
    result = 1
    for i in range(2, n + 1):
        result = lcm(result, i)
    return result


if __name__ == "__main__":
    print(smallest_multiple(20))
