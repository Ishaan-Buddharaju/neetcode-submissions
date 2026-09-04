# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        node = head
        length = 0
        while node:
            length += 1
            node = node.next

        mid = length // 2 # This is the zero indexed last position that isn't moved
        node = head
        idx = 0
        while idx < mid: #stops before the last not moved item
            idx += 1
            node = node.next

        temp = node.next
        node.next = None
        node = temp

        #Reverse the remaining nodes
        prev = None
        while node: 
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        #prev has the new head of the reversed list
        head2 = prev
        
        while head2:
            temp1 = head.next
            temp2 = head2.next
            head.next = head2
            head2.next = temp1
            head = temp1
            head2 = temp2
            



        


        
        
        

    



        

                        


