# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        lst = []
        q = collections.deque()

        q.append(root)

        while q:
            tmp = []
            for _ in range(len(q)):
                node = q.popleft()
                tmp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            lst.append(tmp[-1])
        
        # print(lst)

        # res = []
        # for i in range(len(lst)):
        #     res.append(lst[i][-1])

        return lst
            