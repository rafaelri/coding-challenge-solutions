package xyz.rafaelri.friendcirclequeries;

import java.util.HashMap;
import java.util.Map;

public class FriendCircleQueries {
    static int[] maxCircle(int[][] queries) {
        int[] res = new int[queries.length];
        Map<Integer,Integer> idToPrimary = new HashMap<Integer,Integer>();
        Map<Integer,Integer> primaryToSize = new HashMap<Integer,Integer>();
        int max = 0;
        for (int i=0;i<queries.length;i++) {
            int circleSize = updateCircleSizes(idToPrimary, primaryToSize, queries[i]);
            max = Math.max(max, circleSize);
            res[i]=max;
        }
        return res;
    }
    static int updateCircleSizes(Map<Integer,Integer> idToPrimary, Map<Integer,Integer> primaryToSize, int[] query) {
        int id1 = query[0];
        int id2 = query[1];
        int primary1 = findPrimary(idToPrimary, id1);
        int size1 = findSize(primaryToSize, primary1);
        int primary2 = findPrimary(idToPrimary, id2);
        int size2 = findSize(primaryToSize, primary2);
        if (primary1 != primary2) {
            if (size2> size1) {
                updatePrimary(idToPrimary, primary1, primary2);
                updateSize(primaryToSize, primary2, size1+size2);
                return size1+size2;
            }
            else {
                updatePrimary(idToPrimary, primary2, primary1);
                updateSize(primaryToSize, primary1, size1+size2);
                return size1+size2;
            }
        }
        else {
            if (size1>size2)
                return size1;
            else
                return size2;
        }
    }

    static void updateSize(Map<Integer,Integer> primaryToSize, int id, int size) {
        primaryToSize.put(id, size);
    }

    static int findSize(Map<Integer,Integer> primaryToSize, int id) {
        return primaryToSize.getOrDefault(id, 1);
    }


    static void updatePrimary(Map<Integer,Integer> idToPrimary, int id, int primary) {
        idToPrimary.put(id, primary);
    }

    static int findPrimary(Map<Integer,Integer> idToPrimary, int id) {
        int search = id;
        int response = idToPrimary.getOrDefault(search, search);
        while (response != search) {
            search = response;
            response = idToPrimary.getOrDefault(search, search);
        }
        return response;
    }

}
