class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        time, fresh = 0, 0
        q = collections.deque()

        def addtoq(r, c):
            if (r not in range(rows) or
                c not in range(cols) or
                grid[r][c] != 1):
                return
            nonlocal fresh
            fresh -= 1
            grid[r][c] = 2
            q.append((r, c))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                addtoq(r + 1, c)
                addtoq(r - 1, c)
                addtoq(r, c + 1)
                addtoq(r, c - 1)
            time += 1

        return time if fresh == 0 else -1