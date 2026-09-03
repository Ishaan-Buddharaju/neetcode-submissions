class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return false
        m = len(matrix)
        n = len(matrix[0])
        L = 0
        R = m * n - 1
        while (L <= R): 
            mid = (L + R) // 2 
            rowIdx = mid // n 
            colIdx = mid % n 
            
            num = matrix[rowIdx][colIdx]
            if target > num:
                L = mid + 1
            elif target < num:
                R = mid - 1
            else: 
                return True
        
        return False


