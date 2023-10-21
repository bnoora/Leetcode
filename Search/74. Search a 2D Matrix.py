class Solution:
    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        
        if len(matrix) == 0:
            return False
        
        row = 0
        col = len(matrix[0]) - 1
        
        while row < len(matrix) and col >= 0:

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            elif matrix[row][col] > target:
                col -= 1

                
        return False

