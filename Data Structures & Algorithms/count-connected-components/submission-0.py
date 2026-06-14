class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Create adjacency list
        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visit = set()
        count = 0
        def dfs(i, prev):
            if i in visit or adj[i] == []:
                return
            
            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                dfs(j, i)
            return
        
        for i in range(n):
            if i in visit:
                continue
            count += 1
            dfs(i, -1)
        
        return count