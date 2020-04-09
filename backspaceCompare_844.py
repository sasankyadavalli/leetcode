class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack1 = []
        stack2 = []
        for ele in S:
            if ele is not '#':
                stack1.append(ele)
            elif ele is '#' and len(stack1) != 0:
                stack1.pop()
                
        for ele in T:
            if ele is not '#':
                stack2.append(ele)
            elif ele is '#' and len(stack2) != 0:
                stack2.pop()
                
        if stack1 == stack2:
            return True
        else:
            return False