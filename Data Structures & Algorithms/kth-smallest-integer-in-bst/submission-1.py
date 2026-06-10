# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # self.sortedList = []
        cnt = k
        res = root.val

        def dfs(root):
            nonlocal cnt, res
            if not root:
                return 
            
            dfs(root.left)
            cnt -= 1
            if cnt == 0:
                res = root.val
                return
            # self.sortedList.append(root.val)
            dfs(root.right)

            return
        
        dfs(root)
        # print(self.sortedList)

        return res
        