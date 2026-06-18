class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0
        n = len(heights)
        for i,h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                si, sh = stack.pop()
                ans = max((i - si)*sh, ans)
                start = si
            stack.append((start, h))
        
        for x in stack:
            ans = max(ans, x[1]*(n-x[0]))
        return ans
