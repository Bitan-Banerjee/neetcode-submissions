class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        # Create a stack to hold the brackets
        stk = deque()
        map = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for ch in s:
            if ch in ['(', '{', '[']:
                stk.appendleft(ch)
            elif ch in [')','}',']'] and stk:
                tmp = stk.popleft()
                if map[ch] != tmp:
                    return False
            else:
                return False
        if stk:
            return False
        return True