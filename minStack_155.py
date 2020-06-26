class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minEle = []
    def push(self, x: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(x)
            self.minEle.append(x)
        else:
            self.stack.append(x)
            if self.minEle[-1] >= x:
                self.minEle.append(x)

    def pop(self) -> None:
        ele = self.stack.pop()
        if ele == self.minEle[-1]:
            self.minEle.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minEle[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
