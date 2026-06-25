class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        for t in range(len(temperatures)):
            while stack and temperatures[t] > stack[-1][0]:
                temp, idx = stack.pop()
                res[idx] = t - idx
            stack.append((temperatures[t], t))

        return res