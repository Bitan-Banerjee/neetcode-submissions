"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return 
        val = node.val
        newNode = Node(val)
        self.visited[val] = newNode
        nbrLst = []

        for nbr in node.neighbors:
            if nbr.val in self.visited:
                nbrLst.append(self.visited[nbr.val])
                continue
            nbrLst.append(self.cloneGraph(nbr))
        
        newNode.neighbors = nbrLst

        return newNode
