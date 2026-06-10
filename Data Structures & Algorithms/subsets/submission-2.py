class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        
        def dfs(i):
            if i >= len(nums):
                res.append(subset[:])
                # print("Res :",res)
                return

            # include
            subset.append(nums[i])
            # print(subset)
            dfs(i + 1)

            # exclude
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res
        