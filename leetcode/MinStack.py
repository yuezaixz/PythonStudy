class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        if len(self.min_stack) == 0 or self.min_stack[-1][0] > x:
            self.min_stack.append((x,1))
        elif self.min_stack[-1][0] == x:
            self.min_stack[-1] = (x,self.min_stack[-1][1]+1)
    # @return nothing
    def pop(self):
        top = self.stack.pop()
        if top == self.min_stack[-1][0]:
            if self.min_stack[-1][1] > 1:
                self.min_stack[-1] = (top,self.min_stack[-1][1]-1)
            else:
                self.min_stack.pop()
    # @return an integer
    def top(self):
        return self.stack[-1]
    # @return an integer
    def getMin(self):
        return self.min_stack[-1][0]
if __name__ == "__main__":
    stack = MinStack()
    stack.push(0)
    stack.push(1)
    stack.push(0)
    print stack.getMin()
    stack.pop()
    print stack.getMin()
    stack.pop()
    print stack.getMin()
