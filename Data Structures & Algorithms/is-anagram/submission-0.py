class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): return False

        # Declare additional dictonaries for comparisons
        dict_s = {}
        dict_t = {}

        # Initiate values for the dictonaries
        for i in range(len(s)):
            if s[i] not in dict_s:
                dict_s[s[i]] = 1 
            else: 
                dict_s[s[i]] = dict_s[s[i]] + 1


        for i in range(len(t)):
            if t[i] not in dict_t:
                dict_t[t[i]] = 1 
            else: 
                dict_t[t[i]] = dict_t[t[i]] + 1

        # Check if the dictionaries have different number of distinct characters
        if len(dict_s) != len(dict_t):
            return False

        # Check if the character have similar number of occurance
        else:
            for key in dict_s:
                if key not in dict_t:
                    return False
                elif dict_s[key] != dict_t[key]:
                    return False
                else:
                    continue

        return True

        