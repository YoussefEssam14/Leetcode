import heapq
import math

class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        pq = [-gift for gift in gifts]
        heapq.heapify(pq)                        

        for _ in range(k):
            top = -heapq.heappop(pq)              
            heapq.heappush(pq, -int(math.sqrt(top)))  

        return -sum(pq)                         
