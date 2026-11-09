class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        seen = set()
        m = len(board)
        n = len(board[0])

        def dfs(i, j, charIdx):
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
                down = dfs(i + 1, j, charIdx + 1)
                if down: 
                    return True
            if i - 1 >= 0 and not (i - 1, j) in seen:
                up = dfs(i - 1, j, charIdx + 1)
                if up: 
                    return True
            if j + 1 < n and not (i, j + 1) in seen: 
                right = dfs(i, j + 1, charIdx + 1)
                if right: 
                    return True
            if j - 1 >= 0 and not (i, j - 1) in seen:
                left = dfs(i, j - 1, charIdx + 1)
                if left: 
                    return True
            
            if down or up or right or left: 
                return True
            seen.remove((i,j))
            return False

        
        for i in range(m): 
            for j in range(n): 
                if board[i][j] == word[0]:
                    isWord = dfs(i, j, 0)
                    if isWord: 
                        return True
                    seen = set() # reset seen set each search
        return False

            