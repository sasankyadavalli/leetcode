class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        stack.append(S[0])
        res = ''
        for i in range(1, len(S)):
            if len(stack)== 0:
                stack.append(S[i])
            else:
                if stack[-1] == S[i]:
                    stack.pop()
                else:
                    stack.append(S[i])
                    
        for ele in stack:
            res = res + ele
            
        return res