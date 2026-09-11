# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # def prefix(curr, arr):
        #     if not curr: 
        #         arr.append(None)
        #         return

        #     arr.append(curr.val)
        #     prefix(curr.left, arr)
        #     prefix(curr.right, arr)

        #     return
        
        # subPrefix = []
        # prefix(subRoot, subPrefix)

        # rootPrefix = []
        # prefix(root, rootPrefix)
        # I Dunno pattern matching algos 
        if not subRoot:
            return True
        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))



    
    def isSameTree(self, curr, subCurr):

        if not curr and not subCurr: 
            return True
        elif bool(curr) != bool(subCurr):
            return False

        if curr.val == subCurr.val: 
            return (self.isSameTree(curr.left, subCurr.left) 
                and self.isSameTree(curr.right, subCurr.right))
            
        return False



        

        