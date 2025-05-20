package solutions;

/**
 * Project Euler Problem 6: Sum Square Difference
 *
 * The sum of the squares of the first ten natural numbers is:
 * 1² + 2² + ... + 10² = 385
 *
 * The square of the sum of the first ten natural numbers is:
 * (1 + 2 + ... + 10)² = 55² = 3025
 *
 * Hence the difference between the sum of the squares of the first ten natural
 * numbers and the square of the sum is 3025 - 385 = 2640.
 *
 * Find the difference between the sum of the squares of the first one hundred
 * natural numbers and the square of the sum.
 */
public class Euler006 {
    /**
     * Calculate the difference between the square of the sum and the sum of the
     * squares of the first n natural numbers.
     *
     * @param n Upper bound of the range (inclusive)
     * @return The difference between the square of the sum and the sum of squares
     */
    public static long sumSquareDifference(int n) {
        // Sum of squares: 1² + 2² + ... + n²
        long sumOfSquares = 0;
        for (int i = 1; i <= n; i++) {
            sumOfSquares += (long) i * i;
        }

        // Square of sum: (1 + 2 + ... + n)²
        long sum = (long) n * (n + 1) / 2;  // Using arithmetic series formula
        long squareOfSum = sum * sum;

        return squareOfSum - sumOfSquares;
    }

    public static void main(String[] args) {
        System.out.println(sumSquareDifference(100));
    }
} 