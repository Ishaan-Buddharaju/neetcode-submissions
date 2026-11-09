# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #Recursive
        # Left, Node, Right
        # if not root: 
        #     return []

        # output = []
        # left = self.inorderTraversal(root.left)
        # if left: 
        #     output += left
        # output.append(root.val)
        # right = self.inorderTraversal(root.right)
        # if right:
        #     output += right

        # return output

        # Iterative
        result = []
        stack = []
        curr = root
        while curr != None or len(stack) != 0: 
            while curr: 
                # go left
                stack.append(curr)
                curr = curr.left
            # add the popped to result
            curr = stack.pop()
            result += [curr.val]
            # curr = right
            curr = curr.right
        
        return result

        
        