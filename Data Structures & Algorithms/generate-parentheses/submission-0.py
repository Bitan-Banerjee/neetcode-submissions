class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = []

        def backtrack(opn, cls):
            if opn == cls == n:
                res.append("".join(cur))
                # cur.pop()
                return
            
            if opn < n:
                # we can add opening bracket
                cur.append("(")
                backtrack(opn + 1, cls)
                cur.pop()
            
            if cls < opn:
                # we can add closing bracket
                cur.append(")")
                backtrack(opn, cls + 1)
                cur.pop()
        
        backtrack(0, 0)
        return res