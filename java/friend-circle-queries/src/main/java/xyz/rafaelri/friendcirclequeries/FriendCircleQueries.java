package xyz.rafaelri.friendcirclequeries;

import java.util.HashMap;
import java.util.Map;

public class FriendCircleQueries {
    static int[] maxCircle(int[][] queries) {
        int[] res = new int[queries.length];
        Map<Integer,Integer> idToCircleSize = new HashMap<Integer,Integer>();
        int max = 0;
        for (int i=0;i<queries.length;i++) {
            int circleSize = updateCircleSizes(idToCircleSize, queries[i]);
            max = Math.max(max, circleSize);
            res[i]=max;
        }
        return res;
    }
    static int updateCircleSizes(Map<Integer,Integer> idToCircleSize, int[] query) {
        int id1 = query[0];
        int id2 = query[1];
        int size1 = idToCircleSize.getOrDefault(id1, 1);
        int size2 = idToCircleSize.getOrDefault(id2, 1);
        int sum = size1+size2;
        idToCircleSize.put(id1, sum);
        idToCircleSize.put(id2, sum);
        return sum;
    }
}