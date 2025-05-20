package solutions;

/**
 * Project Euler Problem 5: Smallest Multiple
 *
 * 2520 is the smallest number that can be divided by each of the numbers from
 * 1 to 10 without any remainder.
 *
 * What is the smallest positive number that is evenly divisible by all of the
 * numbers from 1 to 20?
 */
public class Euler005 {
    /**
     * Calculate the Greatest Common Divisor (GCD) of two numbers.
     *
     * @param a First number
     * @param b Second number
     * @return The GCD of a and b
     */
    private static long gcd(long a, long b) {
        return b == 0 ? a : gcd(b, a % b);
    }

    /**
     * Calculate the Least Common Multiple (LCM) of two numbers.
     *
     * @param a First number
     * @param b Second number
     * @return The LCM of a and b
     */
    private static long lcm(long a, long b) {
        return Math.abs(a * b) / gcd(a, b);
    }

    /**
     * Find the smallest positive number that is evenly divisible by all numbers
     * from 1 to n.
     *
     * @param n Upper bound of the range (inclusive)
     * @return The smallest positive number evenly divisible by all numbers from 1 to n
     */
    public static long smallestMultiple(int n) {
        long result = 1;
        for (int i = 2; i <= n; i++) {
            result = lcm(result, i);
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println(smallestMultiple(20));
    }
} 