from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        if head is None or head.next is None:
            return head

        while True:
            slow = slow.next
            fast = fast.next
            if fast.next is None:
                break
            fast = fast.next
            if fast.next is None:
                break
        return slow
