# https://leetcode.com/problems/remove-nth-node-from-end-of-list

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head != None:
            # determine length of linked list by traversing it once
            length = 0
            current = head
            while current:
                current = current.next
                length += 1
            # idx of node to delete
            node_idx = length  - n

            # if node is the head, adjust the head
            if node_idx == 0:
                head = head.next
            else:
                current = head
                prev = None
                idx = 0
                while current and idx != node_idx:
                    prev = current
                    current = current.next
                    idx += 1
                prev.next = current.next
            return head