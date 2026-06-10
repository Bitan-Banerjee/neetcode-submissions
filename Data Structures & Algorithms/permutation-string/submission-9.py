class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        # Initialize a map for s1, and another for window of s2
        map1 = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
        map2 = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}

        # Get the frequencies of s1 and 1st len(s1) elements of s2
        for i in range(len(s1)):
            map1[s1[i]] += 1
            map2[s2[i]] += 1

        matches = 0
        # Now find the matches
        for k in map1:
            if map1[k] == map2[k]: 
                matches += 1
        
        # If all 26 elements of map match
        if matches == 26:
            return True
            
        l = 0
        for r in range(len(s1), len(s2)):
            # Reduce frequency of begenning element
            map2[s2[l]] -= 1
            # Adjust matches accordingly
            if map2[s2[l]] == map1[s2[l]]:
                matches += 1
            elif map1[s2[l]] - map2[s2[l]] == 1:
                matches -= 1
            l += 1

            # If all 26 elements of map match
            if matches == 26:
                return True

            # Increase frequency of last element
            map2[s2[r]] += 1
            # Adjust matches accordingly
            if map2[s2[r]] == map1[s2[r]]:
                matches += 1
            elif map2[s2[r]] - map1[s2[r]] == 1:
                matches -= 1

            # If all 26 elements of map match
            if matches == 26:
                return True

        return False