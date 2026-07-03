class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mapF = {}
        l = 0
        maxL = 0
        maxf = 0

        for r in range(len(s)):
            mapF[s[r]] = 1 + mapF.get(s[r], 0)
            maxf = max(maxf, mapF[s[r]])

            # window len - max freq. char 
            while (r - l + 1) - maxf > k:
                mapF[s[l]] -= 1
                l += 1
            
            maxL = max(maxL, (r - l + 1))


        return maxL
        