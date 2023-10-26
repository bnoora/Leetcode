class Solution:
    def maxAreaOfIsland(self, grid: [[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        vis = set()
        max_area = 0

        def dfs(r, c, max_area):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or (r, c) in vis or grid[r][c] == 0:
                return max_area
            
            vis.add((r, c))
            temp_max_area = max_area
            max_area += 1

            max_area = dfs(r + 1, c, max_area)
            max_area = dfs(r - 1, c, max_area)
            max_area = dfs(r, c + 1, max_area)
            max_area = dfs(r, c - 1, max_area)

            return max(max_area, temp_max_area)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in vis and grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c, 0))
        return max_area




        