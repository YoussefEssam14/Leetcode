import heapq

class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        heaps = [] # max heap for each row
        for row in grid:
            heap = [-val for val in row] # max heap 
            heapq.heapify(heap)
            heaps.append(heap)
        result = 0
        n = len(grid[0])
        for col in range(n):
            curMax = 0
            for heap in heaps:
                val = -heapq.heappop(heap)
                curMax = max(curMax,val)
            result += curMax
        return result