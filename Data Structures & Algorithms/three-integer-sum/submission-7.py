class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        print(nums)

        for i, a in enumerate(nums):
            # Check if current digit has appeared before
            if i > 0 and a == nums[i-1]:
                continue
            
            l, r = i+1, len(nums)-1

            while l < r:
                sum = a + nums[l] + nums[r]
                
                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                else:
                    result.append([a,nums[l],nums[r]])
                    l += 1

                    # Check if new l index is duplicated
                    # if yes then incriment it
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return result