from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        numIslands = 0
        m = len(grid)
        n = len(grid[0])
        def bfs(i, j):
            q = deque()
            q.append((i, j))
            seen.add((i, j))
            while q: 
                for k in range(len(q)):
                    currI, currJ = q.popleft() # (k, l)
                    #down, up, right, left
                    for di, dj in [(1, 0), (-1 , 0), (0, 1), (0, -1)]:
                        if (currI + di < m and 
                            currI + di >= 0 and 
                            currJ + dj < n and 
                            currJ + dj >= 0): 
                            new = (currI + di, currJ + dj)
                            if grid[new[0]][new[1]] == "1" and new not in seen:
                                seen.add(new)
                                q.append(new)
            return
        
        for i in range(m): 
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in seen: 
                    numIslands += 1
                    bfs(i, j)
        return numIslands
