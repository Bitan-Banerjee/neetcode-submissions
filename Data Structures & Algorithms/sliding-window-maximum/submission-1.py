class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()

        res = [] 
        l = r = 0
        while r < len(nums):
            # Pop right elements until new num 
            # is greater then last element of q
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            # Add new num to queue
            q.append(r)

            # when left is out of window 
            # then pop left
            if l > q[0]:
                q.popleft()

            if r - l + 1 == k:
                res.append(nums[q[0]])
                l += 1
            
            r += 1

        return res