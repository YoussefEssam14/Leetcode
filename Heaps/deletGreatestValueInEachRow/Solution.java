import java.util.Collection;
import java.util.Collections;
import java.util.PriorityQueue;

import java.util.PriorityQueue;
import java.util.Collections;
public class Solution {
    public int deleteGreatestValue(int[][] grid){
        int m = grid.length, n = grid[0].length;


        PriorityQueue<Integer>[] heaps = new PriorityQueue[m];
        for (int i = 0; i < m; i++) {
            heaps[i] = new PriorityQueue<>(Collections.reverseOrder());
            for(int val : grid[i])
                heaps[i].offer(val);
        }
        int res = 0;
        for(int col = 0 ; col < n;col++){
            int roundMax = 0;
            for (int j = 0; j < m; j++) {
                roundMax = Math.max(roundMax,heaps[i].poll());
            }
            res += roundMax;
        }
        return res;
    }
}
