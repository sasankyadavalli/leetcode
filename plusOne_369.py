# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        rev_head = self.reverse(head)
        l1 = rev_head
        carry = 1

        while l1:
            if l1.val + carry == 10:
                l1.val = 0
                carry = 1
            else:
                l1.val += carry
                carry = 0
            l1 = l1.next

        if carry == 1:
            node = ListNode(1)
            node.next = self.reverse(rev_head)
            return node
        else:
            return self.reverse(rev_head)



    def reverse(self, head):
        cur = head
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        head = prev
        return head
