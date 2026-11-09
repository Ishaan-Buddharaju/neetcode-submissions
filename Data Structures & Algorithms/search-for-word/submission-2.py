class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        seen = set()
        m = len(board)
        n = len(board[0])

        def bfs(i, j, charIdx):
            # 2 conditions to check each direction
            # - is in bounds
            # - is not in seen
            if board[i][j] != word[charIdx]:
                return False
            elif charIdx + 1 == len(word):
                return True
            seen.add((i,j))
            down, up, right, left = False, False, False, False
            if i + 1 < m and not (i + 1, j) in seen: 
                down = bfs(i + 1, j, charIdx + 1)
            if i - 1 >= 0 and not (i - 1, j) in seen:
                up = bfs(i - 1, j, charIdx + 1)
            if j + 1 < n and not (i, j + 1) in seen: 
                right = bfs(i, j + 1, charIdx + 1)
            if j - 1 >= 0 and not (i, j - 1) in seen:
                left = bfs(i, j - 1, charIdx + 1)
            
            if down or up or right or left: 
                return True
            seen.remove((i,j))
            return False

        
        for i in range(m): 
            for j in range(n): 
                if board[i][j] == word[0]:
                    isWord = bfs(i, j, 0)
                    if isWord: 
                        return True
                    seen = set() # reset seen set each search
        return False

            