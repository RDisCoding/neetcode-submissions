class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')': '(', ']': '[', '}': '{'}
        stack = []
        for ch in s:
            if ch in mapping:
                if not stack: return False
                x = stack.pop()
                if x != mapping[ch]: return False
            else:
                stack.append(ch)
        return not stack