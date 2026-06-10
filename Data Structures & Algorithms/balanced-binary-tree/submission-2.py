# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        # Setting flag variable for output
        self.flag = True

        def height(root):
            if not root: return 0

            lHeight = height(root.left)
            rHeight = height(root.right)

            if abs(lHeight - rHeight) > 1: # and (lHeight != 0 and rHeight != 0):
                self.flag = False

            return max(lHeight, rHeight) + 1
        
        height(root)
        return self.flag
        