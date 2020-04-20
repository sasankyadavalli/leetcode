class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        op, cl = [], []
        for i in range(len(s)):
            a = s[i]
            if a == "(":
                op.append(i)
            elif a == ")":
                if op:
                    op.pop()
                else:
                    cl.append(i)
                    
        
        for i in reversed(cl+op):
            s = s[:i] + s[i+1:]
        return s