# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        
        while(slow and fast and fast.next):
            slow =slow.next
            if (fast.next and fast.next.next):
                fast =fast.next.next
            else:
                return False
            if (slow.val == fast.val):
                return True