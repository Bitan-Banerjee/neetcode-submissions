class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visit = set()
        l, maxL = 0, 0
        window = ''
        for r in range(len(s)):
            while s[r] in visit:
                visit.remove(s[l])
                window = window[1:]
                l += 1
            visit.add(s[r])
            window += s[r]
            maxL = max(maxL, len(window))
        return maxL