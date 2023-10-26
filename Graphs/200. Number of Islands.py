class Solution:
    def numIslands(self, grid: [[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        vis = set()

        def dfs(r, c):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or (r, c) in vis or grid[r][c] == '0':
                return
            
            vis.add((r, c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in vis and grid[r][c] == '1':
                    islands += 1
                    dfs(r, c)
        return islands

            
            

