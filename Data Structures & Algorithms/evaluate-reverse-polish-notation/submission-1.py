class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens: return 0
        stack=[]
        for t in tokens:
            print(stack)
            if t == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(b+a)
            elif t == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif t == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(b*a)
            elif t == "/":
                a = stack.pop()
                b = stack.pop()
                res = b/a
                if res >=0: math.floor(res)
                else: math.ceil(res)
                stack.append(int(res))
            else:
                stack.append(int(t))
            
        return stack[-1]