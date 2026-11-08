# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    runningSum = 0
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: 
            return False
        self.runningSum += root.val
        if not root.left and not root.right and self.runningSum == targetSum: # leaf
            return True
        if self.hasPathSum(root.left, targetSum): 
            return True
        if self.hasPathSum(root.right, targetSum):
            return True
        self.runningSum -= root.val
        return False
            
