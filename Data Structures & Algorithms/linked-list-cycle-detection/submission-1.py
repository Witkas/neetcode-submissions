# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        slow = head
        fast = head

        while fast.next:
            slow = slow.next
            fast = fast.next
            if not fast.next:
                return False
            fast = fast.next
            if slow == fast:
                return True
        return False
