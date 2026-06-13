class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited, cycle = set(), set()
        graph = {}
        res = []

        # Initialize graph with empty values
        graph = {i: [] for i in range(numCourses)}
        # add preq. for each course in graph
        for crs, prq in prerequisites:
            graph[crs].append(prq)

        print(graph)

        def dfs(k):
            if k in cycle:
                return False
            if k in visited:
                return True
            
            cycle.add(k)

            for preq in graph[k]:
                if not dfs(preq):
                    return False
            
            cycle.remove(k)
            visited.add(k)
            res.append(k)
            # visited.remove(k)
            return True
            
        for key in range(numCourses):
            if not dfs(key):
                return []

        return res
        

        