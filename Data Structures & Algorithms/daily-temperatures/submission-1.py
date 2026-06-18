class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                stackT, stacki = stack.pop()
                ans[stacki] = i - stacki
            stack.append((t, i))
        return ans