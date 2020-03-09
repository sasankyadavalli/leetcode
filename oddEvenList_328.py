# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head:
            odd = head
            even_head = even = head.next
            
            while even:
                odd.next = even.next
                if not odd.next:
                    break
                
                odd = odd.next
                even.next = odd.next
                even = even.next
            
            odd.next = even_head
        return head