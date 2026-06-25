from queue import Queue

class MyStack:
    
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x: int) -> None:
        while self.q1.qsize() != 0:
            pop = self.q1.get()
            self.q2.put(pop)
        self.q1.put(x)
        while self.q2.qsize() !=0:
            pop = self.q2.get()
            self.q1.put(pop)

    def pop(self) -> int:
        return self.q1.get()

    def top(self) -> int:
        return self.q1.queue[0]

    def empty(self) -> bool:
        return self.q1.qsize() == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()