class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t.lstrip('-').isdigit():
                stack.append(int(t))
                print(stack)
            else:
                b = stack.pop()
                a = stack.pop()
                match t:
                    case "+":
                        ans = a + b
                    case "-":
                        ans = a - b
                    case "*":
                        ans = a * b
                    case "/":
                        ans = int(float(a)/b)
                        print(ans)
                stack.append(ans)
                print(stack)
        return stack[-1]