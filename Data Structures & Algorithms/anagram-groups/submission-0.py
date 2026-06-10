class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        
        map = {}
        for word in strs:
            key = "".join(sorted(word))
            print(key)
            if key in map:
                map[key].append(word)
            else:
                map[key] = []
                map[key].append(word)

        result = []
        for key in map.keys():
            result.append(map[key])
        
        return result