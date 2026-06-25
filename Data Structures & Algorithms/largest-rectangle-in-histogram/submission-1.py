class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        mx = 0
        for h in range(len(heights)):
            i = h
            while stack and heights[h] <= stack[-1][0]:
                x = stack.pop()
                mx = max(mx, (h - x[1])*x[0])
                i = x[1]
            stack.append((heights[h], i))
            mx = max(mx, heights[h])

        for i in stack:
            mx = max(mx, i[0]*(len(heights) - i[1]))
        
        return mx