"""
Project Euler Problem 6: Sum Square Difference

The sum of the squares of the first ten natural numbers is:
1² + 2² + ... + 10² = 385

The square of the sum of the first ten natural numbers is:
(1 + 2 + ... + 10)² = 55² = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""


def sum_square_difference(n: int) -> int:
    """
    Calculate the difference between the square of the sum and the sum of the
    squares of the first n natural numbers.

    Args:
        n: Upper bound of the range (inclusive)

    Returns:
        int: The difference between the square of the sum and the sum of
        squares
    """
    # Sum of squares: 1² + 2² + ... + n²
    sum_of_squares = sum(i * i for i in range(1, n + 1))

    # Square of sum: (1 + 2 + ... + n)²
    square_of_sum = sum(range(1, n + 1)) ** 2

    return square_of_sum - sum_of_squares


if __name__ == "__main__":
    print(sum_square_difference(100))
