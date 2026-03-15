import java.util.Comparator;
import java.util.PriorityQueue;

public class Solution {
    public int maxProduct(int[] nums) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>;
        for(int num : nums){
            maxHeap.offer(num);
            if(maxHeap.size() > 2)
                maxHeap.poll();
        }
        int x  = maxHeap.poll() - 1;
        int y = maxHeap.poll() - 1;
        return x * y;
    }
}
