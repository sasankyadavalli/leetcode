"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head: return None
        def travel(node):
            while node:
                q = node.next
                if not q: tail = node
                if node.child:
                    node.next = node.child
                    node.child.prev = node
                    t = travel(node.child)
                    if q:
                        q.prev = t
                    t.next= q
                    node.child = None
                node = node.next
            return tail
        travel(head)
        return head
