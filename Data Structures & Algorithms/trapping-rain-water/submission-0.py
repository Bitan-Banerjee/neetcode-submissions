class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft, maxright = [], []
        mx = 0
        res = 0

        # Getting the max left indices
        for i in range(len(height)):
            maxleft.append(mx)
            mx = max(mx,height[i])
        
        mx = 0
        # Getting the max right
        for i in range(len(height)-1, -1, -1):
            maxright.insert(0,mx)
            mx = max(mx,height[i])

        for i in range(len(height)):
            water = min(maxleft[i],maxright[i]) - height[i]
            res += water if water > 0 else 0
            
        return res