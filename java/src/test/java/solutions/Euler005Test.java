import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import solutions.Euler005;

/**
 * Test cases for Project Euler Problem 5: Smallest Multiple
 */
public class Euler005Test {
    @Test
    public void testExampleFromProblem() {
        assertEquals(2520, Euler005.smallestMultiple(10));
    }

    @Test
    public void testSmallNumbers() {
        assertEquals(1, Euler005.smallestMultiple(1));
        assertEquals(2, Euler005.smallestMultiple(2));
        assertEquals(6, Euler005.smallestMultiple(3));
        assertEquals(12, Euler005.smallestMultiple(4));
        assertEquals(60, Euler005.smallestMultiple(5));
    }

    @Test
    public void testActualProblem() {
        assertEquals(232792560, Euler005.smallestMultiple(20));
    }
} 