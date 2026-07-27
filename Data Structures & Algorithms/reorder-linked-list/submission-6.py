# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# [2,4,6,8]
#      s   f
# [2,4,6,8,10]
#      s   f 
# [2,4,6,8,10,12]
#        s       f

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse
        second = slow.next
        slow.next = None
        prev, curr = None, second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev, curr = curr, nxt
        
        newHead = head
        while prev:
            nxt1, nxt2 = head.next, prev.next
            head.next, prev.next = prev, nxt1
            head, prev = nxt1, nxt2
   