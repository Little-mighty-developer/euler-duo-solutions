package solutions;

/**
 * Project Euler Problem 4: Largest Palindrome Product
 *
 * A palindromic number reads the same both ways. The largest palindrome made
 * from the product of two 2-digit numbers is 9009 = 91 × 99.
 *
 * Find the largest palindrome made from the product of two 3-digit numbers.
 */
public class Euler004 {
    /**
     * Check if a number is a palindrome.
     *
     * @param number The number to check
     * @return true if the number is a palindrome, false otherwise
     */
    private static boolean isPalindrome(int number) {
        String str = String.valueOf(number);
        return str.equals(new StringBuilder(str).reverse().toString());
    }

    /**
     * Find the largest palindrome product of two n-digit numbers.
     *
     * @param digits The number of digits in each factor
     * @return The largest palindrome product
     */
    public static int largestPalindromeProduct(int digits) {
        int max = (int) Math.pow(10, digits) - 1;
        int min = (int) Math.pow(10, digits - 1);
        int largestPalindrome = 0;

        for (int i = max; i >= min; i--) {
            for (int j = i; j >= min; j--) {
                int product = i * j;
                if (product < largestPalindrome) {
                    break;
                }
                if (isPalindrome(product)) {
                    largestPalindrome = product;
                }
            }
        }

        return largestPalindrome;
    }

    public static void main(String[] args) {
        System.out.println(largestPalindromeProduct(3));
    }
} 