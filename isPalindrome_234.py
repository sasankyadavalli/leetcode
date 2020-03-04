# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        if head.next is None:
            return True
        prev, slow, fast = None, head , head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        l = self.length(head)
        prev.next = None
        if l % 2 == 1:
            slow = slow.next
        
        l1, l2 = head, slow
        re = self.reverse(l2)
        
        while l1 and re:
            if l1.val != re.val:
                return False
            l1 = l1.next
            re = re.next
        return True
        
        
    def length(self, head):
        if head is None:
            return 0
        count = 0
        while head:
            count += 1
            head = head.next
            
        return count
    
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

# ----------------------------------------------------
# Using Stacks

        if head is None:
            return True
        stack = []
        cur = head
        while cur is not None:
            stack.append(cur.val)
            cur = cur.next
            
        cur = head
        while cur is not None:
            node = stack.pop()
            if node != cur.val:
                return False
            cur = cur.next
            
        return True