class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.mini = float('inf')


    def push(self, val: int) -> None:
        self.stack.append(val)
        if val<= self.mini: 
            self.mini = val
            self.min_stack.append(self.mini)
        print(self.stack)
        print(self.min_stack)

    def pop(self) -> None:
        popped = self.stack.pop()
        if popped == self.min_stack[-1]:
            self.min_stack.pop()
        if not self.min_stack:
            self.mini=float('inf')

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        
