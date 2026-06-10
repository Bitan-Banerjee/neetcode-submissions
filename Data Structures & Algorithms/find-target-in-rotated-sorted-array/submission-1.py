class Solution:
    def bisearch(self,nums,l, r, target):
        # l, r = 0, len(nums) - 1  
        while l <= r:
            m = (l + r)//2
            if target > nums[m]:
                l = m+1
            elif target < nums[m]:
                r = m-1
            else:
                return m   
        return -1

    def search(self, nums: List[int], target: int) -> int:
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
            return self.bisearch(nums,0, len(nums) - 1, target)
        else:
            rslt1= self.bisearch(nums,(m+1),len(nums)-1,target)
            rslt2 = self.bisearch(nums, 0, (m+1),target)
            if rslt1 == rslt2:
                return rslt1
            if rslt1 != -1:
                return rslt1
            else:
                return rslt2