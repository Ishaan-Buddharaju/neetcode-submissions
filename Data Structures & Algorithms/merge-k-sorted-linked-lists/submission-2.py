# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # if (len(lists) == 0):
        #     return None

        def divide(l, r):
            if l > r:
                return None
            if l == r:
                return lists[l]

            mid = l + (r - l) // 2
            left = divide(l, mid)
            right = divide(mid + 1, r)
            return merge(left, right)
        
        # # Can merge sort starting at the conquer step
        def merge(list1, list2):
            l = list1
            r = list2
            dummyResult = ListNode()
            curr = dummyResult
            while (l and r):
                if l.val <= r.val:
                    curr.next = l
                    l = l.next
                else:
                    curr.next = r
                    r = r.next
                curr = curr.next
            
            if l:
                curr.next = l
            else:
                curr.next = r
            
            return dummyResult.next

        if not lists or len(lists) == 0: 
            return None
        return divide(0, len(lists) - 1)
        # i = 1
        # k = len(lists)
        # while (i < k):
        #     for j in range(0, k - i, 2 * i):
        #         lists[j] = merge(lists[j], lists[j + i])
        #     i *= 2
        
        # return lists[0]
