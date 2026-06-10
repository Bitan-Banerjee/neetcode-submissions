# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return None

        self.count = 0

        def dfs(root,mx):
            if not root: return None

            if root.val >= mx:
                mx = root.val
                self.count += 1
                print(root.val)

            dfs(root.left,mx)
            dfs(root.right,mx)

        dfs(root,-101)
        return self.count