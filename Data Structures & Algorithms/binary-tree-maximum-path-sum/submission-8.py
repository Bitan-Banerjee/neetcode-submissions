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
            # if node.val < 0:
            #     max_left = dfs(node.left)
            #     max_right = dfs(node.right)
            #     res[0] = max(max_left + max_right + node.val, res[0])
            #     return 0

            curr = node.val #if node.val>0 else 0

            max_left = dfs(node.left)
            max_right = dfs(node.right)
            curr_max = curr + max_left + max_right

            res[0] = max(curr_max, res[0])

            if max(max_left,max_right) + curr < 0:
                return 0
            else:
                return max(max_left,max_right) + curr


        dfs(root)
        return res[0]