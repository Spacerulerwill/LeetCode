# https://leetcode.com/problems/middle-of-the-linked-list/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast:
            fast = fast.next
            if not fast:
                break
            fast = fast.next
            slow = slow.next
        return slow