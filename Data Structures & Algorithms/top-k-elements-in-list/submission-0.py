class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        # Creating a map to find the frequency of each element
        for i in nums:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1

        # Creating a frequency map
        fmap = {}
        for i in map:
            if map[i] in fmap:
                fmap[map[i]].append(i)
            else:
                fmap[map[i]] = [i]

        # We need to sort the fmap based on keys
        sorted_keys = sorted(fmap.items(),key = lambda x: x[0],reverse=True)
        print(sorted_keys)

        # now we can creat a list for sorted elements based on frequency
        flist = []
        for i in sorted_keys:
            flist.extend(i[1])

        result = [flist[i] for i in range(k)]
        return result