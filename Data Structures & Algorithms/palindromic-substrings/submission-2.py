class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            res += self.isPal(i, i, s)
            res += self.isPal(i, i + 1, s)
        
        return res
    
    def isPal(self, l, r, s):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        
        return res