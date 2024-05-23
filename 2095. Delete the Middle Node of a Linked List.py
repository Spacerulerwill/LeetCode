# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        prev = None
        while fast:
            prev = fast
            fast = fast.next
            if not fast:
                break
            prev = fast
            fast = fast.next
            slow = slow.next
        if not prev:
            return None
        else:
            return head
        print(prev.val)