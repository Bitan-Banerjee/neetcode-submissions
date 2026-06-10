class Solution:
    def trap(self, height: List[int]) -> int:
        left, right= 0, len(height)-1
        maxleft, maxright = height[left], height[right]
        res = 0
        
        while left < right:
            if maxleft < maxright:
                left += 1
                maxleft = max(maxleft,height[left])
                res += maxleft - height[left]
            else:
                right -= 1
                maxright = max(maxright,height[right])
                res += maxright - height[right]

        return res