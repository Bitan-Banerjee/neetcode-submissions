# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binarySearch(self,root,key):
        rslt = []
        if key.val == root.val:
            return [key]
        
        rslt.append(root)
        if key.val < root.val:
            rslt.extend(self.binarySearch(root.left,key))
        else:
            rslt.extend(self.binarySearch(root.right,key))

        return rslt

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return root
        
        # Binary search
        pathp = self.binarySearch(root,p)
        pathq = self.binarySearch(root,q)

        pathmap = {i.val: True for i in pathp}
        
        lca = root
        for i in pathq:
            if i.val in pathmap:
                lca = i
            else:
                break
        
        return lca