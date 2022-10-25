from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = []


a3: ListNode = ListNode(3)
a2: ListNode = ListNode(4, a3)
a1: ListNode = ListNode(2, a2)

b3: ListNode = ListNode(4)
b2: ListNode = ListNode(6, b3)
b1: ListNode = ListNode(5, b2)
result = Solution.addTwoNumbers(a1, b1)
