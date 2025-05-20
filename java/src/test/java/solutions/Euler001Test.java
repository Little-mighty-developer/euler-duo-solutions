import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import solutions.Euler001;

/**
 * Test cases for Project Euler Problem 1: Multiples of 3 and 5
 */
public class Euler001Test {
    @Test
    public void testExampleFromProblem() {
        assertEquals(23, Euler001.sumMultiplesOf3And5(10));
    }

    @Test
    public void testZeroLimit() {
        assertEquals(0, Euler001.sumMultiplesOf3And5(0));
    }

    @Test
    public void testSmallLimit() {
        assertEquals(0, Euler001.sumMultiplesOf3And5(1));
        assertEquals(0, Euler001.sumMultiplesOf3And5(2));
        assertEquals(0, Euler001.sumMultiplesOf3And5(3));
        assertEquals(3, Euler001.sumMultiplesOf3And5(4));
        assertEquals(3, Euler001.sumMultiplesOf3And5(5));
        assertEquals(8, Euler001.sumMultiplesOf3And5(6));
    }

    @Test
    public void testActualProblem() {
        assertEquals(233168, Euler001.sumMultiplesOf3And5(1000));
    }
} 