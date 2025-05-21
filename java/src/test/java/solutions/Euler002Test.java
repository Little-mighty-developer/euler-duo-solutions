import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import solutions.Euler002;

/**
 * Test cases for Project Euler Problem 2: Even Fibonacci Numbers
 */
public class Euler002Test {
    @Test
    public void testSmallLimit() {
        assertEquals(0, Euler002.sumEvenFibonacciNumbers(1));
        assertEquals(2, Euler002.sumEvenFibonacciNumbers(2));
        assertEquals(2, Euler002.sumEvenFibonacciNumbers(3));
        assertEquals(2, Euler002.sumEvenFibonacciNumbers(4));
        assertEquals(2, Euler002.sumEvenFibonacciNumbers(5));
        assertEquals(10, Euler002.sumEvenFibonacciNumbers(8));
    }

    @Test
    public void testMediumLimit() {
        assertEquals(44, Euler002.sumEvenFibonacciNumbers(34));
        assertEquals(44, Euler002.sumEvenFibonacciNumbers(35));
    }

    @Test
    public void testActualProblem() {
        assertEquals(4613732, Euler002.sumEvenFibonacciNumbers(4_000_000));
    }
} 