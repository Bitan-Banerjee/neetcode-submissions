class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        minHeap = self.nums.copy()
        heapq.heapify(minHeap)
        srtd = []
        while minHeap:
            srtd.append(heapq.heappop(minHeap))
        
        median = 0
        l = len(srtd)
        if l%2 == 0:
            median = (srtd[l//2] + srtd[l//2 - 1])/2
        else:
            median = float(srtd[l//2])
        return median
        