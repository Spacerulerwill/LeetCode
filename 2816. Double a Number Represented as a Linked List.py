# https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # helper function to reverse linked list
        def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
            prev = None
            current = head
            while current:
                next = current.next
                current.next = prev
                prev = current
                current = next
            return prev
        # reverse the list
        reversed = reverse_list(head)

        # iterate over, doubling digits adding carry, and setting new carry
        current, previous = reversed, None
        carry_digit = 0
        while current:
            digit_sum = (current.val * 2) + carry_digit
            carry_digit = digit_sum // 10
            digit_sum %= 10
            current.val = digit_sum
            previous, current = current, current.next

        #add last carry digit if there is one remaining
        if carry_digit != 0:
            previous.next = ListNode(carry_digit)

        # reverse the list again
        return reverse_list(reversed)

if __name__ == "__main__":
    solution = Solution()
    print(solution.doubleIt(ListNode(1, ListNode(8, ListNode(9)))))