# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        d = {}
        while headA is not None:
            d[headA] = headA.next
            headA = headA.next
        while headB is not None:
            if headB in d:
                return headB
            headB = headB.next
        return None