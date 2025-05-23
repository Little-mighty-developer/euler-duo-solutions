package solutions;

/**
 * Project Euler Problem 1: Multiples of 3 and 5
 *
 * If we list all the natural numbers below 10 that are multiples of 3 or 5,
 * we get 3, 5, 6 and 9. The sum of these multiples is 23.
 *
 * Find the sum of all the multiples of 3 or 5 below 1000.
 */
public class Euler001 {
    /**
     * Calculate the sum of all multiples of 3 or 5 below the given limit.
     *
     * @param limit The upper bound (exclusive)
     * @return The sum of all multiples of 3 or 5 below the limit
     */
    public static int sumMultiplesOf3And5(int limit) {
        int sum = 0;
        for (int i = 1; i < limit; i++) {
            if (i % 3 == 0 || i % 5 == 0) {
                sum += i;
            }
        }
        return sum;
    }

    public static void main(String[] args) {
        System.out.println(sumMultiplesOf3And5(1000));
    }
} 