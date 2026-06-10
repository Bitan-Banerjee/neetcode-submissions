class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""

        mapS, mapT = {}, {}
        res = ""
        have= 0 
        length = float("infinity")

        # Initialize target map
        for c in t:
            mapT[c] = 1 + mapT.get(c, 0)
        need = len(mapT) 
        # Start sliding window
        l = 0
        for r in range(len(s)):
            c = s[r]
            mapS[c] = 1 + mapS.get(c, 0)

            if c in mapT and mapS[c] == mapT[c]:
                have += 1

            # If maps are matching, store the min sumstring in res
            while have == need: 
                currentlen = r - l + 1
                if currentlen < length:
                    length = currentlen
                    res = s[l:r+1]
                
                mapS[s[l]] -= 1
                if s[l] in mapT and mapS[s[l]] < mapT[s[l]]:
                    have -= 1
                l += 1

        return res