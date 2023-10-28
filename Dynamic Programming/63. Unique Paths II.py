class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: [[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        if obstacleGrid[1][1] == 1 and ROWS == 1 and COLS == 1:
            return 0
        if obstacleGrid[ROWS-1][COLS-1] == 1:
            return 0
        memo = {(ROWS-1, COLS-1): 1}

        def dfs(r, c):
            if r == ROWS or c == COLS or obstacleGrid[r][c] == 1:
                return 0
        
            if (r, c) in memo:
                return memo[(r, c)]
            memo[(r, c)] = dfs(r+1, c) + dfs(r, c+1)
            return memo[(r, c)]
        return dfs(0, 0)


        
        
