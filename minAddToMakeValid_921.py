class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        s = ""
        stack = []
        d = {")": "("}
        for i in S:
            if i == "(":
                stack.append(i)
            else:
                if len(stack) > 0:
                    if d[i] == stack[-1]:
                        stack.pop()
                else:
                    s = s + i
                    
        if len(stack) == 0:
            return len(s)
        else:
            while len(stack) > 0:
                s = s + stack.pop()
                
            return len(s)