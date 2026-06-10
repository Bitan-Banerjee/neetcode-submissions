class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         
        l = len(nums)
        dict = {}

        for i in range(0,l):
            if nums[i] in dict:
                return True
            else:
                dict[nums[i]] = 1
        
        return False