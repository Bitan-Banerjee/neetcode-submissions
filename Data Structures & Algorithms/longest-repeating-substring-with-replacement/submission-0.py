class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        map = {}
        for i in range(ord('A'),ord('Z')+1):
            map[chr(i)] = 0
        # print(map)

        l = 0
        res = 0
        for r in range(len(s)):
            # Check if current window is valid if valid then incriment by 1
            # window_length - lenght_of_most_frequent <= k
            # Window_length = r-l+1
            # We would get maxFrequency like below
            map[s[r]] += 1
            # what is the max frequency of a char in current window?
            maxFr = 0
            for key in map:
                if map[key] > maxFr:
                    maxFr = map[key]
            
            # Check Valid window now
            if (r - l + 1) - maxFr <= k:
                # Window is valid
                res = max(res,(r - l + 1))

            else:
                # Decriment the left pointer value on map
                # slide left pointer
                map[s[l]] -= 1
                l += 1
        # print(map)
        return res