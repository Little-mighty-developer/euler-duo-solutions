import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import solutions.Euler006;

/**
 * Test cases for Project Euler Problem 6: Sum Square Difference
 */
public class Euler006Test {
    @Test
    public void testExampleFromProblem() {
        assertEquals(2640, Euler006.sumSquareDifference(10));
    }

    @Test
    public void testSmallNumbers() {
        assertEquals(0, Euler006.sumSquareDifference(1));
        assertEquals(4, Euler006.sumSquareDifference(2));
        assertEquals(22, Euler006.sumSquareDifference(3));
    }

    @Test
    public void testActualProblem() {
        assertEquals(25164150, Euler006.sumSquareDifference(100));
    }
} 