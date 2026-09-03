# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # visited = {} # stores node: idx
        # index = 0
        # while head != None:
        #     if head.next in visited:
        #         return True
        #     visited[head] = index
        #     head = head.next
        #     index += 1
        
        # return False
        slow = head
        fast = head
        index = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            index += 1
            if fast == slow:
                return True


        return False

            