import collections
class Solution:
    def isValidSudoku(self, board: [[str]]) -> bool:
        col_set = collections.defaultdict(set)
        row_set = collections.defaultdict(set)
        box_set = collections.defaultdict(set)

        for k in range(9):
            for c in range(9):
                if board[k][c] == ".": continue
                if board[k][c] in row_set[k]: return False
                if board[k][c] in col_set[c]: return False
                if board[k][c] in box_set[(k//3, c//3)]: return False

                row_set[k].add(board[k][c])
                col_set[c].add(board[k][c])
                box_set[(k//3, c//3)].add(board[k][c])
        return True




        