class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> maxH = new PriorityQueue<>(Collections.reverseOrder());
        for (int s : stones) maxH.offer(s);

        while (maxH.size() > 1) {
            int y = maxH.poll();
            int x = maxH.poll();
            if (y != x) maxH.offer(y - x);
        }

        return maxH.isEmpty() ? 0 : maxH.peek();
    }
}