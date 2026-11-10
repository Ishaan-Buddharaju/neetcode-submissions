from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:


        q = deque()
        m = len(grid)
        n = len(grid[0])
        seen = set()
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
                    seen.add((i,j))
                elif grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        minutes = -1
        while q: 
            minutes += 1
            for k in range(len(q)):
                curri, currj = q.popleft()
                grid[curri][currj] = 2
                for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
                    if (0 <= curri + di < m and 0 <= currj + dj < n): 
                        ni, nj = curri + di, currj + dj
                        if grid[ni][nj] == 1 and (ni, nj) not in seen: 
                            q.append((ni, nj))
                            seen.add((ni, nj))
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        return minutes
