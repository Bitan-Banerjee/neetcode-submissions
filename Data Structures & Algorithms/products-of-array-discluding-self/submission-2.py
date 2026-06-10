class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        a = nums
        prefix, suffix = [], []

        # Create prefix array from rolling product
        prd = 1
        for i in range(len(a)):
            prefix.append(prd)
            prd *= a[i]

        # Create suffix array from rolling product
        prd = 1
        suffix = [0] * len(a)
        for i in range(len(a)-1, -1, -1):
            suffix[i] = prd
            prd *= a[i]


        for i in range(len(nums)):
            output.append(prefix[i]*suffix[i])

        return output