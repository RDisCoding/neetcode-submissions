class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for ops in operations:
            print((stack, ops))
            if ops == "C":
                stack.pop()
            elif ops == "D":
                popped = stack[-1]
                stack.append(2*popped)
            elif ops == "+":
                b = stack[-1]
                a = stack[-2]
                stack.append(a+b)
            else:
                stack.append(int(ops))
        
        return sum(stack)
