class Node:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self):
        self.root = Node()

    def addword(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Node()
            curr = curr.children[ch]
        curr.word = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Building the Trie
        obj = Trie()
        for word in words:
            obj.addword(word)
        root = obj.root

        # Preping the search
        ROWS, COLS = len(board), len(board[0])
        res, visited = set(), set()

        def dfs(r, c, cur, node):
            if (r >= ROWS or c >= COLS or r < 0 or c < 0 or
                (r,c) in visited or
                board[r][c] not in node.children):
                # print(board[r][c], node.children)
                return
            
            # Updating the variables
            visited.add((r,c))
            cur += board[r][c]
            node = node.children[board[r][c]]
            # print(cur)

            if node.word:
                res.add(cur)

            dfs(r + 1, c, cur, node)
            dfs(r, c + 1, cur, node)
            dfs(r - 1, c, cur, node)
            dfs(r, c - 1, cur, node)

            visited.remove((r,c))

        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r, c, "", root)
        return list(res)
        