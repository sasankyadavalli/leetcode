class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = ['(', '[', '{']
        mem = {')': '(', '}': '{', ']': '['}
        for ele in s:
            if ele in open:
                stack.append(ele)
            else:
                if not stack:
                    return False
                if mem[ele] == stack[-1]:
                    stack.pop()
                else:
                    return False
                
        if len(stack) > 0:
            return False
        return True