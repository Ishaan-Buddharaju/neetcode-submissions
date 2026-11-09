# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS
        # if not root: 
        #     return []

        # output = []
        # q = deque()
        # q.append(root)
        # while q: 
        #     output.append(q[-1].val) # rightmost because insertion is left to right
        #     for i in range(len(q)): 
        #         curr = q.popleft()
        #         if curr.left:
        #             q.append(curr.left)
        #         if curr.right:
        #             q.append(curr.right)
        # return output

        # DFS
        output = []
        def dfs(root, depth):
            if not root: 
                return None
            
            if depth == len(output):
                output.append(root.val)
                
            dfs(root.right, depth + 1)
            dfs(root.left, depth + 1)
            return 

        dfs(root, 0)
        return output



        