class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0]*n
        q = deque()

        for r in range(n):
            while q and temperatures[q[-1]] < temperatures[r]:
                i = q.pop()
                ans[i] = r-i
            q.append(r)
        
        return ans