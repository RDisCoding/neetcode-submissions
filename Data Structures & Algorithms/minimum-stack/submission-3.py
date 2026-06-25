class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)            
        if self.minstack:
            if val <= self.minstack[-1]:
                self.minstack.append(val)
        else:
            self.minstack.append(val)

    def pop(self) -> None:
        x = self.stack.pop()
        print(x)
        print(self.minstack)
        if self.minstack and self.minstack[-1] == x:
            self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1] if self.minstack else 0

