class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.nums.sort()

    def findMedian(self) -> float:
        median = 0
        l = len(self.nums)
        if l%2 == 0:
            median = (self.nums[l//2] + self.nums[l//2 - 1])/2
        else:
            median = float(self.nums[l//2])
        return median
        