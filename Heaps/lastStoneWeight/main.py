import heapq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        maxH = [-s for s in stones]
        heapq.heapify(maxH)
        while len(maxH) > 1:
            y = -heapq.heappop(maxH)
            x = -heapq.heappop(maxH)
            if y != x:
                heapq.heappush(maxH,-(y-x))
        return -maxH[0] if maxH else 0