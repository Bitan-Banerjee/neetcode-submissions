class MinStack:

    def __init__(self):
        self.stk= []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        if self.minStack:
            mn = min(self.minStack[-1], val)
        else:
            mn = val

        self.minStack.append(mn)
        return self

    def pop(self) -> None:
        self.stk.pop()
        self.minStack.pop()
        
    def top(self) -> int:
        if self.stk:
            return self.stk[-1]

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]

        
