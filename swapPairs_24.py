class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        while cur and cur.next:
            nextNode = cur.next.next
            cur.next.next = cur
            if prev:
                prev.next = cur.next
            else:
                head = head.next
                
            prev = cur
            cur.next = nextNode
            cur = nextNode
            
        return head