class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        for i in range(len(nums)):
            if i == 0:
                prd = nums[1]
            else:
                prd = nums[0]

            for j in range(len(nums)):
                if j == i:
                    continue
                if i == 0 and j == 1:
                    continue
                if i != 0 and j == 0:
                    continue
                prd = prd * nums[j]

            output.append(prd)
        
        return output