class MinStack:
    def __init__(self):
        self.stack = []
        self.min = pow(2,31)

    def push(self, val: int) -> None:
        diff = val - self.min
        self.stack.append(diff)
        if diff < 0:
            self.min = val

    def pop(self) -> None:
        diff = self.stack.pop()
        if diff < 0:
            self.min = self.min - diff

    def top(self) -> int:
        diff = self.stack[-1]
        if diff < 0:
            return self.min
        return diff + self.min

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

m = MinStack()
m.push(-2)
m.push(0)
m.push(-3)
print(m.getMin())
m.pop()
print(m.top())
print(m.getMin())