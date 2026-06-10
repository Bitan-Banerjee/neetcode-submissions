class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        m = {
                '2': 'abc',
                '3': 'def',
                '4': 'ghi',
                '5': 'jkl',
                '6': 'mno',
                '7': 'pqrs',
                '8': 'tuv',
                '9': 'wxyz',
                '0': '+'
            }
        
        res = []
        comb = []

        def dfs(i):
            if i >= len(digits):
                temp = "".join(comb.copy())
                res.append(temp)
                return
            s = m[digits[i]]
            for j in range(len(s)):
                comb.append(s[j])
                dfs(i + 1)
                comb.pop()
        
        dfs(0)
        return res