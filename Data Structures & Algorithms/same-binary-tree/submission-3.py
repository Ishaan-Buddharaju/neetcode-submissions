# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #traverse and compare

        def prefix(curr, arr):
            if not curr:
                arr.append(None)
                return

            arr.append(curr.val)
            prefix(curr.left, arr)
            prefix(curr.right, arr)

            return
        arr_p = []
        arr_q = []
        prefix(p, arr_p)
        prefix(q, arr_q)

        if len(arr_p) != len(arr_q):
            return False

        for i in range(len(arr_p)):
            if arr_p[i] != arr_q[i]:
                return False
        return True

            
        