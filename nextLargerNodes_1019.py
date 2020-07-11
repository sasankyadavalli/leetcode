# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        index = 0
        ans = []
        stack = []
        while head is not None:
            ans.append(0)
            cur_value = head.val
            while stack and stack[-1][0] < cur_value:
                pair = stack.pop()
                ans[pair[1]] = cur_value

            stack.append((cur_value, index))
            index += 1
            head = head.next

        return ans
