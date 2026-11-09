# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Iterative
        #NLR
        if not root: 
            return []
        output = []
        stack = [root]
        while stack: 
            # pop and add to output
            curr = stack.pop()
            output.append(curr.val)
            # setup right
            # - if right exists
            if curr.right: 
            # - push onto stack
                stack.append(curr.right)
            # setup left
            # - if left exists
            if curr.left:
            # - push onto stack
                stack.append(curr.left)
        
        return output
