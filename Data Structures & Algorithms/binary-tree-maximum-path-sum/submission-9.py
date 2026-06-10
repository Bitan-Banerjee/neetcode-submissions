# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(node):
            if not node:
                return 0

            max_left = dfs(node.left)
            max_right = dfs(node.right)
            curr_max = node.val + max_left + max_right

            res[0] = max(curr_max, res[0])
            max_path = max(max_left,max_right) + node.val 

            return max_path if max_path > 0 else 0


        dfs(root)
        return res[0]