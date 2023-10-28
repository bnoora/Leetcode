from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: [[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        vis = set()
        q = deque()
        q.append((0, 0))
        vis.add((0, 0))

        length = 1
        if grid[0][0] == 1 or grid[ROWS - 1][COLS - 1] == 1:
            return -1

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length
                moves = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
                for move in moves:
                    new_r = r + move[0]
                    new_c = c + move[1]
                    if new_r < 0 or new_r >= ROWS or new_c < 0 or new_c >= COLS or grid[new_r][new_c] == 1 or (new_r, new_c) in vis:
                        continue
                    else:
                        q.append((new_r, new_c))
                        vis.add((new_r, new_c))
            length += 1
        return length if length != 0 else -1
