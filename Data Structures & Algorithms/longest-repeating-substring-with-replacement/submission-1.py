class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mapF = {}
        maxF = 0
        maxL = 0
        l = 0
        for r in range(len(s)):
            # if map[s[r]] is present return freq else return 1
            mapF[s[r]] = 1 + mapF.get(s[r], 0)
            maxF = max(mapF.values())

            # len(substr) - maxF <= k
            if (r - l + 1) - maxF <= k:
                # max leng = max(maxL, len(substr))
                maxL = max(maxL, (r - l + 1))
            else:
                mapF[s[l]] -= 1
                l += 1

        return maxL