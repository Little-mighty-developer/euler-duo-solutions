"""
Project Euler Problem 2: Even Fibonacci Numbers

Each new term in the Fibonacci sequence is generated by adding the previous two
terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not
exceed four million, find the sum of the even-valued terms.
"""


def sum_even_fibonacci(limit: int) -> int:
    """
    Calculate the sum of even Fibonacci numbers up to the given limit.

    Args:
        limit (int): The upper bound (exclusive) for Fibonacci numbers

    Returns:
        int: The sum of even Fibonacci numbers below the limit

    Raises:
        ValueError: If the limit is negative
    """
    if limit < 0:
        raise ValueError("Limit must be a non-negative integer")

    # Initialize first two Fibonacci numbers
    a, b = 1, 2
    total = 0

    while b < limit:
        # Add even numbers to total
        if b % 2 == 0:
            total += b
        # Generate next Fibonacci number
        a, b = b, a + b

    return total


def main():
    """Main function to solve and display the answer."""
    limit = 4_000_000
    result = sum_even_fibonacci(limit)
    print(f"The sum of even Fibonacci numbers below {limit} is: {result}")


if __name__ == "__main__":
    main()
