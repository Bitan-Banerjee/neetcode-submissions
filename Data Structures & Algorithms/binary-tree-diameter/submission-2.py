# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    RES = 0
    def maxHeight(self, root):
        if not root: return 0

        # Getting the left and right hight of the current node.
        left_ht = self.maxHeight(root.left)
        right_ht = self.maxHeight(root.right)

        # Diameter = maxLeftHeight + maxReightHeight
        diameter = left_ht + right_ht
        self.RES = max(diameter, self.RES)

        # Return the max height
        return 1 + max(left_ht, right_ht)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        self.maxHeight(root)
        
        # Return the max height
        return self.RES
        