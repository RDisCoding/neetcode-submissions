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
                        if a<0 and b<0:
                            ans = a//b
                        elif a<0 or b<0:
                            ans = -1 * (abs(a)//abs(b))
                        else:
                            ans = a // b
                        print(ans)
                stack.append(ans)
                print(stack)
        return stack[-1]