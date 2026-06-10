# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return 'N'
        res = []

        q = collections.deque()
        q.append(root)
        while q:
            current = q.popleft()
            if not current:
                res.append('N')
                continue
            res.append(str(current.val))
            q.append(current.left)
            q.append(current.right)

        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        if vals[0] == 'N':
            return None
        root = TreeNode(val = int(vals[0]))
        q = deque([root])
        index = 1
        while q:
            node = q.popleft()
            if vals[index] != 'N':
                node.left = TreeNode(int(vals[index]))
                q.append(node.left)
            index += 1
            if vals[index] != 'N':
                node.right = TreeNode(int(vals[index]))
                q.append(node.right)
            index += 1
        return root


