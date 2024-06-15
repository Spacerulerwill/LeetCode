# https://leetcode.com/problems/remove-nodes-from-linked-list/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        elements = [] # monotonic decreasing stack
        while head:
            while elements and elements[-1] < head.val:
                elements.pop()
            elements.append(head.val)
            head = head.next
        
        if not elements:
            return None

        list_node = ListNode(elements[0])
        current = list_node
        for i in range(1, len(elements)):
            new = ListNode(elements[i])
            current.next = new
            current = new
        return list_node
        
        

if __name__ == "__main__":
    solution = Solution()
    node = ListNode(5, ListNode(2, ListNode(13, ListNode(3, ListNode(8)))))
    print(solution.removeNodes(node))