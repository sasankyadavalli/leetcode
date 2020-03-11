# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(float("-inf"))
        dummy.next = head
        prev = dummy
        cur = head
        while cur and cur.next:
            if (val := cur.val) == cur.next.val:
                while cur and cur.val == val:
                    cur = cur.next
                prev.next = cur
            else:
                prev = cur
                cur = cur.next
                
        return dummy.next

