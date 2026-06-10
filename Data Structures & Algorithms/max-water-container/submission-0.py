class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        maxarea = 0

        while l < r:
            area = (r-l) * min(heights[l], heights[r])

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
            
            maxarea = max(maxarea,area)
        
        return maxarea