class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        solutionSpace = [[1 for i in range(n)] for j in range(m)]
        
        for i in range(1, m):
            for j in range(1, n):
                solutionSpace[i][j] = solutionSpace[i - 1][j] + solutionSpace[i][j - 1]
        
        return solutionSpace[m - 1][n - 1]
                