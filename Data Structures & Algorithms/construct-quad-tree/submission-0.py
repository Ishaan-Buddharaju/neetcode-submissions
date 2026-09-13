"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        # split the quad tree grid and call recursively
        if self.canBeLeaf(grid):
            result = Node(val=grid[0][0], isLeaf=True)
            return result

        n = len(grid)
        half = n // 2
        
        result = Node(isLeaf = False)
        for i in range(0, n, n // 2):
            for j in range(0, n, n // 2):
                quadrant = [row[j:j + half] for row in grid[i:i + half]]
                quadNode = None
                if self.canBeLeaf(quadrant):
                    quadNode = Node(val=quadrant[0][0], isLeaf=True)
                else: 
                    quadNode = self.construct(quadrant)
                
                if i == 0 and j == 0: 
                    result.topLeft = quadNode
                elif i == half and j == 0:
                    result.bottomLeft = quadNode
                elif i == 0 and j == half:
                    result.topRight = quadNode
                else:
                    result.bottomRight = quadNode
        
        return result
                
                

        # topLeft = [row[0: n // 2] for row in grid[0: n // 2]]
        # botLeft = [row[0: n // 2] for row in grid[n // 2 - 1:]]

        # topRight = [row[n // 2 - 1:] for row in grid[0: n // 2]]
        # botRight = [row[n // 2 - 1:] for row in grid[n // 2 - 1:]]

    def canBeLeaf(self, grid: List[List[int]]) -> bool:
        assert(grid != None)

        check = grid[0][0]

        for row in grid: 
            for num in row:
                if num != check: 
                    return False
        
        return True

