import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        minH = []
        for n in nums:
            heapq.heappush(minH,n)
            if len(minH) > k:
                heapq.heappop(minH)
        return minH[0]
