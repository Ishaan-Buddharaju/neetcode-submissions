class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colSets = [set() for _ in range(9)]
        rowSets = [set() for _ in range(9)]
        boxSets = [[set() for _ in range(3)] for _ in range(3)] 

        for i in range(9):
            for j in range(9):
                curr = board[i][j]
                if curr == '.':
                    continue

                if curr in colSets[j]:
                    return False
                else:
                    colSets[j].add(curr)

                if curr in rowSets[i]:
                    return False  
                else:
                    rowSets[i].add(curr)

                if curr in boxSets[i // 3][j // 3]:
                    return False 
                else:
                    boxSets[i // 3][j // 3].add(curr)

        return True
                
                
