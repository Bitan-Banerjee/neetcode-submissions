class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        l, r = 0, 1
        maxdiff= prices[r] - prices[l]

        while r <= len(prices) - 1:
            crntdiff = prices[r] - prices[l]
            maxdiff = max(maxdiff, crntdiff)
            if prices[r] <= prices[l]:
                l = r
                r += 1
            else:
                r += 1
        
        if maxdiff < 0:
            return 0

        return maxdiff