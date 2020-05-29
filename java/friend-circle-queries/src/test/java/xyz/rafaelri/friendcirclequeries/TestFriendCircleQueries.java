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

    @Test
    public void testFourConnectionsDistinctBounds() {
        assertThat(FriendCircleQueries.maxCircle(new int[][]{new int[]{1, 2}, new int[]{3, 4},new int[]{1, 4}, new int[]{5,6}, new int[]{3,6}}), equalTo(new int[]{2, 2, 4, 4, 8}));
    }

    @Test
    public void testTwoConnectionsThreeElements() {
        assertThat(FriendCircleQueries.maxCircle(new int[][]{new int[]{1, 2}, new int[]{1, 3}}), equalTo(new int[]{2, 3}));
    }

}