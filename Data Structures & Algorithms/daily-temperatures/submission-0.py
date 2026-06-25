class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans  = [0]*len(temperatures)
        stack = [(temperatures[0],0)]
        for t in range(1, len(temperatures)):
            while stack and temperatures[t] > stack[-1][0]:
                x = stack.pop()
                ans[x[1]] = t - x[1]
            stack.append((temperatures[t], t))

        return ans