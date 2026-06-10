class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_map = {}
        t_map = {}

        for c in s:
            s_map[c] = (s_map[c] + 1) if c in s_map else 1

        for c in t:
            t_map[c] = (t_map[c] + 1) if c in t_map else 1

        return s_map == t_map