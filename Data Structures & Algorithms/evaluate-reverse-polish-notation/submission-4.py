class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = deque()

        for i in tokens:
            if i in ["+","-","*","/"]:
                b = stk.pop()
                a = stk.pop()
                if i == "+":
                    stk.append(a+b)
                elif i == "-":
                    stk.append(a-b)
                elif i == "*":
                    stk.append(a*b)
                else:
                    stk.append(int(a/b))
            else:
                stk.append(int(i))
        
        return stk[0]