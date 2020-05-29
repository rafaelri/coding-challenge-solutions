package xyz.rafaelri.friendcirclequeries;

import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.*;

import org.junit.Test;
public class TestFriendCircleQueries {
    @Test
    public void testSingleConnection() {
        assertThat(FriendCircleQueries.maxCircle(new int[][]{new int[]{1, 2}}), equalTo(new int[]{2}));
    }
    @Test
    public void testTwoSeparateConnections() {
        assertThat(FriendCircleQueries.maxCircle(new int[][]{new int[]{1, 2}, new int[]{3, 4}}), equalTo(new int[]{2, 2}));
    }
    @Test
    public void testThreeConnectionsBoundFinal() {
        assertThat(FriendCircleQueries.maxCircle(new int[][]{new int[]{1, 2}, new int[]{3, 4},new int[]{1, 4}}), equalTo(new int[]{2, 2, 4}));
    }

}