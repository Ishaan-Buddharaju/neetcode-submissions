# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        pathMax = float('-inf')
        count = 0
        def dfs(root):
            nonlocal pathMax
            nonlocal count

            if not root:
                return

            maxCopy = pathMax
            if root.val >= pathMax:
                count += 1
                pathMax = root.val
            dfs(root.left)
            dfs(root.right)
            pathMax = maxCopy # restore before unwinding
            return

        dfs(root)
        return count
