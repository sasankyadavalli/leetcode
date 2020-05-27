# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        p = dummy = ListNode(0)
        dummy.next = head
        for _ in range(m - 1):
            p = p.next
        cur = p.next
        pre = None
        for _ in range(n - m + 1):
            cur.next, pre, cur = pre, cur, cur.next
        p.next.next = cur
        p.next = pre
        return dummy.next