# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Bottom up choices
        # left, right
        # or LNR
        # then Left max without splitting + self
        # or right max without splitting + self
        # or left + self + right

        self.res = root.val
        def dfs(root):
            if not root: 
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            left = max(left, 0)
            right = max(right, 0)
            self.res = max(self.res, root.val + left + right)

            return root.val + max(left, right)
        dfs(root)
        return self.res

        # max of curr is max of left + curr or curr then
        # update curr accordingly
        # max of curr is max of curr and curr + right



            