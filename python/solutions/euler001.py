"""
Project Euler Problem 1: Multiples of 3 or 5

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def sum_multiples_of_3_and_5(limit: int) -> int:
    """
    Calculate the sum of all multiples of 3 or 5 below the given limit.

    Args:
        limit (int): The upper bound (exclusive) for finding multiples

    Returns:
        int: The sum of all multiples of 3 or 5 below the limit

    Raises:
        ValueError: If the limit is negative
    """
    if limit < 0:
        raise ValueError("Limit must be a non-negative integer")
    return sum(num for num in range(limit) if num % 3 == 0 or num % 5 == 0)


def main():
    """Main function to solve and display the answer."""
    limit = 1000
    result = sum_multiples_of_3_and_5(limit)
    print(f"The sum of all multiples of 3 or 5 below {limit} is: {result}")


if __name__ == "__main__":
    main()
