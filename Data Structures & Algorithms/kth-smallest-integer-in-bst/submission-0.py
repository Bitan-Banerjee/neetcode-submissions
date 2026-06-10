# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.sortedList = []

        def dfs(root):
            if not root:
                return 
            
            dfs(root.left)
            self.sortedList.append(root.val)
            dfs(root.right)

            return
        
        dfs(root)
        print(self.sortedList)

        return self.sortedList[k-1]
        