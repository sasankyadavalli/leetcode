class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """

        self.stack = []
        self.maxEle = []
    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.maxEle or x >= self.maxEle[-1]:
            self.maxEle.append(x)

    def pop(self) -> int:
        if self.stack[-1] == self.maxEle[-1]:
            self.maxEle.pop()

        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        if self.maxEle:
            return self.maxEle[-1]
    def popMax(self) -> int:
        a = []
        while self.stack[-1] != self.maxEle[-1]:
            a.append(self.stack[-1])
            self.stack.pop()

        out = self.stack.pop()
        self.maxEle.pop()
        while a:
            self.push(a[-1])
            a.pop()
        return out



# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
