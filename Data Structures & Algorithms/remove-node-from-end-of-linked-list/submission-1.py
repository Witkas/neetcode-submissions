# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        l, r = dummy, head
        for _ in range(n):
            r = r.next
        while r:
            l, r = l.next, r.next
        
        # Remove
        l.next = l.next.next
        return dummy.next