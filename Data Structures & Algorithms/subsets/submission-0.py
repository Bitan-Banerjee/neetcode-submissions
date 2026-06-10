class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset[:])
                return
            
            # Include scenario
            subset.append(nums[i])
            dfs(i+1)

            # Exclude scenario
            subset.pop()
            dfs(i+1)

            return
        
        dfs(0)
        return res
        