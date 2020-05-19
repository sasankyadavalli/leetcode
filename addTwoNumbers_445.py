# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = self.reverse(l1)
        l4 = self.reverse(l2)
        carry = 0
        dummy = now = ListNode(0)
        while l3 or l4 or carry:
            if l3:
                carry += l3.val
                l3 = l3.next
            if l4:
                carry += l4.val
                l4 = l4.next
            now.next = ListNode(carry%10)
            now = now.next
            carry //= 10
            
        return self.reverse(dummy.next)
        
    def reverse(self, l):
        prev = None
        cur = l
        while cur is not None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev