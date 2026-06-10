class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)

        if l == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        left, right = 0, l-1
        mid = (right - left)//2
        print(mid)

        while left < right:
            print(left, right, mid)
            if nums[mid] == target:
                return mid
            
            elif nums[mid] > target:
                right = mid
                mid = left + ((right - left)//2)

            else:
                left = mid
                mid = left + ((right - left)//2)

            if (right - left) == 1:
                if nums[right] == target:
                    return right
                elif nums[left] == target:
                    return left
                else:
                    return -1
        
        return -1