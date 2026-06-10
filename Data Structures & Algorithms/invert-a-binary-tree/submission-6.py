# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # If root is null
        if root == None: return

        # If we reach the leaf node then return
        if root.left == None and root.right == None:
            return root
        
        # lets switch the left with the right
        temp = root.left
        root.left = root.right
        root.right = temp
        # print(root.left.val, root.right.val)

        # Now recursively call the function 
        # with the right and left node
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
        