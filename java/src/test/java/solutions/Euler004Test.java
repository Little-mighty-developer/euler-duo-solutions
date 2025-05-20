import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import solutions.Euler004;

/**
 * Test cases for Project Euler Problem 4: Largest Palindrome Product
 */
public class Euler004Test {
    @Test
    public void testExampleFromProblem() {
        assertEquals(9009, Euler004.largestPalindromeProduct(2));
    }

    @Test
    public void testSingleDigit() {
        assertEquals(9, Euler004.largestPalindromeProduct(1));
    }

    @Test
    public void testActualProblem() {
        assertEquals(906609, Euler004.largestPalindromeProduct(3));
    }

    @Test
    public void testFourDigits() {
        assertEquals(99000099, Euler004.largestPalindromeProduct(4));
    }
} 