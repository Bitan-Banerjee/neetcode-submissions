class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l+r)//2

            if l == r and r == 0:
                break
            if nums[m] > nums[r] and (r-m) == 1:
                break

            if nums[m] > nums[r]:
                l = m
            else:
                r = m

        if m == 0 and r == 0:
            return nums[0]
        else:
            return nums[m+1]