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
        obj = Trie()
        root = obj.root

        # Create trie for each word in the words list
        for word in words:
            obj.addword(word)
        
        # Variables for backtracking dfs
        res, visited = set(), set()
        ROWS, COLUMNS = len(board), len(board[0])
        
        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLUMNS or
                (r,c) in visited or board[r][c] not in node.children):
                return

            visited.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.word:
                res.add(word)
            
            dfs(r, c + 1, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r - 1, c, node, word)

            visited.remove((r,c))
    
        for r in range(ROWS):
            for c in range(COLUMNS):
                dfs(r, c, root, "")

        return list(res)
        