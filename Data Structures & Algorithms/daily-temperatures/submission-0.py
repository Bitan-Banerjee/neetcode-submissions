class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stk = deque()
        result = [0 for i in range(len(temp))]

        for i in range(len(temp)):
            if stk:
                if temp[i] <= stk[-1][0]:
                    stk.append((temp[i],i))
                else:
                    while stk and temp[i] > stk[-1][0]:
                        # First update result array
                        topIdx = stk[-1][1]
                        days = i - topIdx
                        result[topIdx] = days

                        # next pop the top of the stack
                        stk.pop()
                    stk.append((temp[i],i))
            else:
                stk.append((temp[i],i))
        
        return result