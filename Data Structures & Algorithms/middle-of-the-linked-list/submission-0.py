# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr != None:
            length += 1
            curr = curr.next
        curr = head
        i = 0
        target = length // 2 
        while i != target:
            i += 1
            curr = curr.next
        return curr
            
        
