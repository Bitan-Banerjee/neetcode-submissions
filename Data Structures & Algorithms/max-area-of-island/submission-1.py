class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: 
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        maxArea = 0

        def dfs(row, col):
            if (row not in range(rows) or
                col not in range(cols) or
                grid[row][col] != 1 or
                (row, col) in visited ):
                return 0
            visited.add((row,col))
            print(row, col)
            ar = 1

            directions = [[-1,0], [1,0], [0,-1], [0,1]]
            for dr, dc in directions:
                r, c = (row + dr), (col + dc)
                ar += dfs(r, c)
            
            return ar


        for r in range(rows):
            for c in range(cols):
                if (grid[r][c] == 1 and
                    (r, c) not in visited):
                    print(r, c)
                    area = dfs(r,c)
                    maxArea = max(maxArea, area)
        
        return maxArea

        