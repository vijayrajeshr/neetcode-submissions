class MinStack:

    def __init__(self):
        self.stack = []
        self.minstac = []
        

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.minstac:
            self.minstac.append(value)  
        else:
            minval = min(value,self.minstac[-1])
            self.minstac.append(minval)
            

    def pop(self) -> None:
        # If the popped item is the current minimum, remove it from min_stack as well
        if self.stack.pop() == self.minstac[-1]:
            self.minstac.pop()
        else:
            self.minstac.pop()
            
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstac[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()