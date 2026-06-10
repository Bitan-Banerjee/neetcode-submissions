class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur):
            if sum(cur) == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or sum(cur) > target:
                return
            
            # Include scenario
            cur.append(nums[i])
            dfs(i, cur)

            # Exclude scenario
            cur.pop()
            dfs(i + 1, cur)
        
        dfs(0, [])
        return res