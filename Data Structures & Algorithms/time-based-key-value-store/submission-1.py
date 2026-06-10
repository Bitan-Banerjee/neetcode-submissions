class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key not in self.map:
            self.map[key] = [(value, timestamp)]
        else:
            self.map[key].append((value,timestamp))
            

    def get(self, key: str, timestamp: int) -> str:
        if (key not in self.map) or (self.map[key] == []):
            return ""
        else: 
            lst = self.map[key]
            print(lst)
            rslt = self.search(lst,timestamp)
            if rslt == -1:
                return ""
            return rslt[0]


    def search(self, lst, timestamp):
        # This is a binary search fn.
        # Set left and right pointer
        l, r = 0, len(lst)-1
        prev = 0

        while l <= r:
            m = (l+r)//2

            if lst[m][1] < timestamp:
                prev = m
                l = m + 1
            elif lst[m][1] > timestamp:
                r = m - 1
            else:
                return lst[m]
        
        # Check if previous value is updated form the default value
        if prev == 0:
            if lst[prev][1] < timestamp:
                return lst[prev]
            else:
                return -1

        return lst[prev]