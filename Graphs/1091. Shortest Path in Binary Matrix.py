from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: [[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        vis = set()
        q = deque()
        q.append((0, 0))
        vis.add((0, 0))

        length = 0

        while q:
            r, c = q.popleft()
            if r == ROWS - 1 and c == COLS - 1:
                return length + 1
            moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            for move in moves:
                new_r = r + move[0]
                new_c = c + move[1]
                if 0 <= new_r < ROWS and 0 <= new_c < COLS and grid[new_r][new_c] == 0 and (new_r, new_c) not in vis:
                    q.append((new_r, new_c))
                    vis.add((new_r, new_c))
            length += 1
