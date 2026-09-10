# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # computer subtree heights. 
        # if abs(L - R) > 1 return false
        isBalanced = True
        def dfs(curr):
            if not curr:
                return 0 
            
            L = dfs(curr.left)
            R = dfs(curr.right)
            if L == -1 or R == -1: 
                return -1
        
            if abs(L - R) > 1:
                return -1
            
            return max(L, R) + 1
        
        result = dfs(root)
        if result == -1: 
            isBalanced = False
        return isBalanced
        

        