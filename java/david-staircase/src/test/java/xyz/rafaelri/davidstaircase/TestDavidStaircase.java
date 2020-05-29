package xyz.rafaelri.davidstaircase;

import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.*;

import org.junit.Test;
public class TestDavidStaircase {
    @Test
    public void testSingleStepStaircase() {
        assertThat(DavidStaircase.stepPerms(1), equalTo(1));
    }

    @Test
    public void testTwoStepStaircase() {
        assertThat(DavidStaircase.stepPerms(2), equalTo(2));
    }

    @Test
    public void testThreeStepStaircase() {
        assertThat(DavidStaircase.stepPerms(3), equalTo(4));
    }

    @Test
    public void testFourStepStaircase() {
        assertThat(DavidStaircase.stepPerms(4), equalTo(7));
    }

    @Test
    public void testSevenStepStaircase() {
        assertThat(DavidStaircase.stepPerms(7), equalTo(44));
    }

}