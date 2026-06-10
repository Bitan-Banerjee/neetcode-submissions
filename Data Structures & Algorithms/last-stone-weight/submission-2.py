class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-i for i in stones]
        heapq.heapify(maxHeap)
        print(len(maxHeap))

        while len(maxHeap) > 1:
            a = heapq.heappop(maxHeap)
            b = heapq.heappop(maxHeap)
            
            sub = a - b
            if sub < 0:
                heapq.heappush(maxHeap, sub)
            
            print(maxHeap)
        
        if len(maxHeap) == 0:
            return 0
            
        return abs(maxHeap[0])
        