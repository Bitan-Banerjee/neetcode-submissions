class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(n):
            # if len(n) <= 1:
            #     return max(0, n[0])
            rob1, rob2 = 0, 0

            for i in range(len(n)):
                temp = rob2
                rob2 = max(rob2, (rob1 + n[i]))
                rob1 = temp
            
            return rob2
        
        return max(nums[0],
                    helper(nums[:-1]), 
                    helper(nums[1:]))