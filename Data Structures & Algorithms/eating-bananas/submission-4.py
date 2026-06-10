class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mx = max(piles)
        if h == len(piles):
            return mx
        
        l, r = 1, mx
        k = 0
        while l <= r:
            m = (l+r) // 2
            hours = 0
            # print(l, r)
            # print(f"Mid {m}")

            for i in piles:
                if i <= m:
                    hours += 1
                elif i%m == 0:
                    hours += i//m
                else:
                    hours += 1 + (i//m)
            
            # print(f"Hours {hours}")
            if hours <= h:
                r = m - 1
                k = m
            else:
                l = m + 1

        return k