# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        represent if subtree has p and has q through bits
        - 0: 00 is false and false
        - 1: 01 is false and True thus it has q
        - 2: 10 is True and false thus it has p
        - 3: 11 is True and True thus it has both p and q

        then return the LCA node in the second position of the tuple
        '''

        def dfs(root):
            if not root:
                return [0, None]
            
            left = [0, None]
            if p.val < root.val and q.val < root.val:
                left = dfs(root.left)
                if left[0] == 3:
                    return left

            right = [0, None]
            if p.val > root.val and q.val > root.val:
                right = dfs(root.right)
                if right[0] == 3:
                    return right
            return [3, root]
            # res = [0, None]
            # res[0] = left[0] | right[0]
            # if root == p:
            #     res[0] |= 1
            # if root == q: 
            #     res[0] |= 2
            # if res[0] == 3: 
            #     return [3, root]

            # return res
        res = dfs(root)

        return res[1]

            

        