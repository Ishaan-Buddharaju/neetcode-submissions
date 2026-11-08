# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(val = -1, next=head)
        p1 = head
        p2 = head
        prev = None
        dist = 0
        while p1:
            if dist < n:
                p1 = p1.next
                dist += 1
            else: 
                p1 = p1.next
                prev = p2
                p2 = p2.next
        
        if prev == None: 
            return head.next
        else: 
            prev.next = p2.next
            p2.next = None

        return dummy.next
        