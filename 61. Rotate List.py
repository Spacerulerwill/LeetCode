# https://leetcode.com/problems/rotate-list/
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        # obtain length of linked list
        length = 0
        current = head
        while True:
            length += 1
            if current.next:
                current = current.next
            else:
                break
        #obtain actual shift amount
        k %= length
        # if the shift would do nothing just return
        if k == 0:
            return head
        # set end to point to beginning - the linked list is now in cycle
        current.next = head
        # traverse the list again to get to the right point to break the cycle
        traverse_next = length - k
        for _ in range(traverse_next):
            current = current.next
        next_save = current.next
        current.next = None
        return next_save

if __name__ == "__main__":
    solution = Solution()
    list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    solution.rotateRight(list, 1)