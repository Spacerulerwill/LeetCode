# https://leetcode.com/problems/merge-nodes-in-between-zeros/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        new_head = None
        new_tail = new_head
        curr = head.next
        sum = 0
        while curr and curr.next:
            sum += curr.val
            if curr.next.val == 0:
                new_node = ListNode(sum)
                if not new_head:
                    new_head = new_node
                    new_tail = new_node
                else:
                    new_tail.next = new_node
                    new_tail = new_node
                sum = 0
            curr = curr.next
        return new_head