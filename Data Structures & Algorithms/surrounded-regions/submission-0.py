class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Intution is whatever 'O' is found in the edges,
        and whatever 'O' is part of that connect group,
        we mark those cells as visited.
        Next, whatever 'O' remain, those are the 'O's that we
        want to turn to 'X'
        """
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r, c):
            if (r not in range(rows) 
                or c not in range(cols) or
                (r, c) in visited 
                or board[r][c] != 'O'):

                return
            visited.add((r,c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        def search_rows(r, cols):
            for c in range(cols):
                if board[r][c] == 'O' and (r,c) not in visited:
                    dfs(r, c)

        def search_cols(rows, c):
            for r in range(rows):
                if board[r][c] == 'O' and (r,c) not in visited:
                    dfs(r, c)
        
        # search in 1st and last row
        search_rows(0, cols)
        search_rows(rows - 1, cols)

        # search in 1st and last column
        search_cols(rows, 0)
        search_cols(rows, cols - 1)

        # By now we would have all the unsorrounded regions
        # and their respective cells inside of visited
        print(visited)

        for r in range(rows):
            for c in range(cols):
                print(board[r][c])
                if board[r][c] == 'O' and (r,c) not in visited:
                    print("entered")
                    board[r][c] = 'X'
                    print("new ", board[r][c])
