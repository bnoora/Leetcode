from collections import deque
class Solution:
    def orangesRotting(self, grid: [[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        vis = set()
        q = deque()
        mins = 0
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                    vis.add((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0
        if fresh != 0 and len(q) == 0:
            return -1

        while q and fresh > 0:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()
                moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                for move in moves:
                    new_r = r + move[0]
                    new_c = c + move[1]
                    if new_r < 0 or new_r >= ROWS or new_c < 0 or new_c >= COLS or grid[new_r][new_c] == 0 or (new_r, new_c) in vis:
                        continue
                    if grid[new_r][new_c] == 1:
                        fresh -= 1
                        grid[new_r][new_c] = 2
                        q.append((new_r, new_c))
                        vis.add((new_r, new_c))
                    else:
                        q.append((new_r, new_c))
                        vis.add((new_r, new_c))
            mins += 1
        
        if fresh != 0:
            return -1
        return mins

        