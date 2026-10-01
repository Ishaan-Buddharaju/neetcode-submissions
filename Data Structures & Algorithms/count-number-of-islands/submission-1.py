class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        islandCount = 0
        m = len(grid)
        n = len(grid[0])

        def bfs(i, j):
            val = grid[i][j] 
            if (i,j) in seen:
                return
            
            seen.add((i,j))
            if val == "0": 
                return

            if j - 1 >= 0:
                bfs(i, j - 1)
            if j + 1 < n:
                bfs(i, j + 1)
            if i - 1 >= 0:
                bfs(i - 1, j)
            if i + 1 < m: 
                bfs(i + 1, j)


            # if i - 1 < 0 and j - 1 < 0: 
            #     bfs(i, j + 1) # r
            #     bfs(i + 1, j)# down
            # elif i - 1 < 0 and j + 1 >= n:
            #     bfs(i, j - 1)# left
            #     bfs(i + 1, j)# down
            # elif i + 1 >= m and j + 1 >= n: 
            #     bfs(i - 1, j)# up
            #     bfs(i, j - 1)# left
            # elif i + 1 >= m and j - 1 < 0: 
            #     bfs(i - 1, j)# up
            #     bfs(i, j + 1)# right
            # elif i - 1 < 0: 
            #     bfs(i, j - 1)# l
            #     bfs(i, j + 1)# r
            #     bfs(i + 1, j)# d
            # elif i + 1 >= m: 
            #     bfs(i, j + 1)
            #     bfs(i, j - 1)# l
            #     bfs(i - 1, j)# u
            # elif j - 1 < 0: 
            #     bfs(i - 1, j)# u
            #     bfs(i - 1, j)# d
            #     bfs(i, j + 1)# r
            # elif j + 1 >= n:
            #     bfs(i - 1, j)# u
            #     bfs(i + 1, j)# d 
            #     bfs(i, j - 1)# l
            # else:
            #     bfs(i, j + 1) # r
            #     bfs(i, j - 1) # l
            #     bfs(i - 1, j) # u
            #     bfs(i + 1, j) # d

        for i in range(m):
            for j in range(n):
                if (i,j) in seen: 
                    continue # Skip

                val = grid[i][j]
                if val == "0": 
                    seen.add((i,j))
                    continue
                
                bfs(i, j)
                print("here " + str(val))
                islandCount += 1

        return islandCount



    