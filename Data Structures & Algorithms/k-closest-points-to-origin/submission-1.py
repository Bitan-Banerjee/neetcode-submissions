import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        res = []

        for x, y in points:
            dis = 0 - math.sqrt(x*x + y*y)
            heapq.heappush(maxHeap, [dis, x, y])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        while k > 0:
            d, x, y = heapq.heappop(maxHeap)
            res.append([x, y])
            k -= 1
        return res
        