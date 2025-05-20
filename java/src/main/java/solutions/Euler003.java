package solutions;

/**
 * Project Euler Problem 3: Largest Prime Factor
 *
 * The prime factors of 13195 are 5, 7, 13 and 29.
 *
 * What is the largest prime factor of the number 600851475143?
 */
public class Euler003 {
    /**
     * Find the largest prime factor of a number.
     *
     * @param number The number to find the largest prime factor of
     * @return The largest prime factor
     */
    public static long largestPrimeFactor(long number) {
        long largestFactor = 1;
        long divisor = 2;

        while (number > 1) {
            while (number % divisor == 0) {
                largestFactor = divisor;
                number /= divisor;
            }
            divisor++;
            if (divisor * divisor > number) {
                if (number > 1) {
                    largestFactor = number;
                }
                break;
            }
        }

        return largestFactor;
    }

    public static void main(String[] args) {
        System.out.println(largestPrimeFactor(600_851_475_143L));
    }
} 