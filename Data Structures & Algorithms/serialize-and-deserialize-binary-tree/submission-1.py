# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(node):
            if not node:
                res.append('N')
                return
            
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        print(res)
        return ",".join(res)
            
            

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        print(vals)
        i = 0

        def dfs():
            nonlocal i
            # print(i)
            if vals[i] == 'N':
                return
            
            node = TreeNode(int(vals[i]))
            print("val",node.val)
            i += 1
            node.left = dfs()
            i += 1
            node.right = dfs()
            return node

        root = dfs()
        return root
