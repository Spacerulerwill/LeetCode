from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        tail = temp
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            digit1 = 0 if l1 == None else l1.val
            digit2 = 0 if l2 == None else l2.val
            sum = digit1 + digit2 + carry
            digit = sum % 10
            carry = sum // 10

            new_node = ListNode(digit)
            tail.next = new_node
            tail = tail.next

            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
        result = temp.next
        return result