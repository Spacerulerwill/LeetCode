# https://leetcode.com/problems/linked-list-cycle/

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        fast = head
        slow = head
        while True:
            #advance fast pointer twice
            fast = fast.next
            if not fast:
                return False
            if fast is slow:
                return True
            fast = fast.next
            # if fast pointer is null, no cycle
            if not fast:
                return False
            # if fast pointer and slow pointer meet, there is a cycle
            if fast is slow:
                return True
            #advance slow pointer
            slow = slow.next
            # if fast and slow pointer meet, there is a cycle
            if slow is fast:
                return True