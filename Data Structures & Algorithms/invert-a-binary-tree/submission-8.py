# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # If root is null
        if not root: return

        # If we reach the leaf node then return
        if not root.left and not root.right:
            return root
        
        # Switch the left with the right
        root.right,root.left = root.left, root.right

        # Recursion: Call invertTree with the right and left node
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
        