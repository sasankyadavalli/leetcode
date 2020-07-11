# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None

        if head.next == None:
            return head
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        actual = k % length

        if k == 0 or actual == 0:
            return head

        prev = None
        cur = head
        ind = 0
        while cur:
            if ind == length-actual:
                prev.next = None
                new_head = cur
                cur2 = new_head
                while cur2.next is not None:
                    cur2 = cur2.next
                cur2.next = head
                head = new_head
                return head
            prev = cur
            cur = cur.next

            ind += 1
