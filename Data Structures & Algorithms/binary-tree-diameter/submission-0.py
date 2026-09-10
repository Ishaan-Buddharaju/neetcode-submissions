# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter of sub tree is the height of left + height of right subtree

        self.diameter = 0

        def height(curr):
            if not curr: 
                return 0
            
            L = height(curr.left)
            R = height(curr.right)
            self.diameter = max(self.diameter, L + R)
            return max(L, R) + 1

        height(root)
        return self.diameter
        




