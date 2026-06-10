# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self,root):
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = collections.deque()

        level= 0
        height = self.height(root)
        rslt = [[] for _ in range(height)]

        queue.append([root,level])
        while queue:
            node, level = queue.popleft()
            rslt[level].append(node.val)

            if node.left:
                queue.append([node.left, level + 1])
            if node.right:
                queue.append([node.right, level + 1])

        return rslt
            
        