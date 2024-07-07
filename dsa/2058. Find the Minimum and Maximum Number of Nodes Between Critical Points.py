# https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> list[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        min_dist = float("inf")
        prev = head.val
        middle = head.next.val
        current = head.next.next
        first_critical_index = None
        current_critical_index = None
        i = 2
        while current:
            # local maximum
            if middle > current.val and middle > prev:
                if first_critical_index is None:
                    first_critical_index = i -1
                # also update min
                new_critical_index = i -1
                if current_critical_index is not None:
                    min_dist = min(min_dist, new_critical_index - current_critical_index)
                current_critical_index = new_critical_index
            # local minimum
            elif middle < current.val and middle < prev:
                if first_critical_index is None:
                    first_critical_index = i - 1
                # also update min
                new_critical_index = i -1
                if current_critical_index is not None:
                    min_dist = min(min_dist, new_critical_index - current_critical_index)
                current_critical_index = new_critical_index
            prev = middle
            middle = current.val
            current = current.next
            i += 1
        if any(x is None for x in (current_critical_index, first_critical_index)) or min_dist == float("inf"):
            return [-1, -1]
        max_dist = current_critical_index - first_critical_index
        return [min_dist, max_dist]
