import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        mp = {}
        res = []

        for x, y in points:
            dis = 0 - math.sqrt(x*x + y*y)
            distance.append(dis)
            if dis not in mp:
                mp[dis] = [[x,y]]
            else: 
                mp[dis].append([x,y])

        print(mp)
        heapq.heapify(distance)

        while len(distance) > k:
            heapq.heappop(distance)
        print(distance)

        for d in distance:
            res.append(mp[d].pop())


        return res
        