class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set()
        negDiag = set()

        res = []
        cur = [['.']*n for i in range(n)]

        def backtrack(r):
            if r >= n:
                temp = ["".join(s) for s in cur]
                res.append(temp)
                return
            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                
                # update the sets
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                cur[r][c] = 'Q'

                backtrack(r + 1)

                # revert
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                cur[r][c] = '.'



        backtrack(0)
        return res