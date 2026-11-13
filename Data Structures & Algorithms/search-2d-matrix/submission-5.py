class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        total = m * n
        l = 0
        r = total - 1

        while (l <= r):
            midpoint = l + (r - l) // 2
            row = midpoint // n
            col = midpoint % n
            if matrix[row][col] == target: 
                return True
            elif matrix[row][col] < target: 
                l = midpoint + 1
            else: 
                r = midpoint - 1
            
        return False


