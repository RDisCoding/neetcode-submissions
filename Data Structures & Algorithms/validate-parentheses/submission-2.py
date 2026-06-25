class Solution:
    def isValid(self, s: str) -> bool:
        h = {
            ']': '[',
            '}': '{',
            ')': '('
        }
        stack = []
        for c in s:
            if c in h.values():
                stack.append(c)
            else:
                if not stack: return False
                x = stack.pop()
                if x != h[c]: return False
        return True if not stack else False