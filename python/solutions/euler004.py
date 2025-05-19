"""
Project Euler Problem 4: Largest Palindrome Product

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindrome(n: int) -> bool:
    """
    Check if a number is a palindrome.

    Args:
        n: The number to check

    Returns:
        bool: True if the number is a palindrome, False otherwise
    """
    return str(n) == str(n)[::-1]


def largest_palindrome_product() -> int:
    """
    Find the largest palindrome made from the product of two 3-digit numbers.

    Returns:
        int: The largest palindrome product
    """
    largest_palindrome = 0
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            product = i * j
            if product < largest_palindrome:
                break
            if is_palindrome(product):
                largest_palindrome = product
    return largest_palindrome


if __name__ == "__main__":
    print(largest_palindrome_product())
