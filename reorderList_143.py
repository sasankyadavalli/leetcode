# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None:
            return

        new = self.middle(head)
        new_rev = self.reverse(new)
        self.merge(head, new_rev)

    def reverse(self, head):
        cur = head
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        return prev

    def middle(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        new_list = slow.next
        slow.next = None

        return new_list

    def merge(self, head1, head2):
        cur1 = head1
        cur2 = head2
        dummy = ListNode(-1)
        while cur1 or cur2:
            if cur1:
                dummy.next = cur1
                cur1 = cur1.next
                dummy = dummy.next
            if cur2:
                dummy.next = cur2
                cur2 = cur2.next
                dummy = dummy.next

        return dummy.next
            
