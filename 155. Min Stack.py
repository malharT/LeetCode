class MinStack:

    def __init__(self):
        self.min = None
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minstack) == 0:
            self.minstack.append(len(self.stack)-1)
        else:
            if self.stack[self.minstack[-1]] > val:
                self.minstack.append(len(self.stack)-1)

    def pop(self) -> None:
        if self.minstack[-1] == len(self.stack) - 1:
            self.minstack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.minstack[-1]]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()