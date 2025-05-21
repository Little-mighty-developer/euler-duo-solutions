import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import solutions.Euler003;

/**
 * Test cases for Project Euler Problem 3: Largest Prime Factor
 */
public class Euler003Test {
    @Test
    public void testExampleFromProblem() {
        assertEquals(29, Euler003.largestPrimeFactor(13195));
    }

    @Test
    public void testPrimeNumbers() {
        assertEquals(2, Euler003.largestPrimeFactor(2));
        assertEquals(3, Euler003.largestPrimeFactor(3));
        assertEquals(5, Euler003.largestPrimeFactor(5));
        assertEquals(7, Euler003.largestPrimeFactor(7));
    }

    @Test
    public void testCompositeNumbers() {
        assertEquals(5, Euler003.largestPrimeFactor(10));
        assertEquals(7, Euler003.largestPrimeFactor(14));
        assertEquals(13, Euler003.largestPrimeFactor(26));
    }

    @Test
    public void testActualProblem() {
        assertEquals(6857, Euler003.largestPrimeFactor(600_851_475_143L));
    }
} 