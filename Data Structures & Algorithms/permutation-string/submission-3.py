class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map1 = {}
        for ch in s1:
            if ch in map1:
                map1[ch] += 1
            else:
                map1[ch] = 1
        
        map2 = {}
        l = 0
        for r in range(len(s2)):
            if s2[r] in map2:
                map2[s2[r]] += 1
            else:
                map2[s2[r]] = 1       
            # If substring length matched with target
            if r - l + 1 == len(s1):
                # print(map1, map2)
                # check if substiring matched target
                if map1 == map2:
                    return True
                else:
                    # If substring doesnt match then slide window by 1
                    # remove the last emelemt if frequency = 0 else decrient frequency by 1
                    map2[s2[l]] -= 1
                    if map2[s2[l]] == 0:
                        map2.pop(s2[l])
                    l += 1
        return False