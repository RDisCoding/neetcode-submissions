class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for h in range(len(heights)):
            i = h
            while stack and heights[h] <= stack[-1][1]:
                start, height = stack.pop()
                res = max(res, (h - start) * height)
                i = start
            stack.append((i, heights[h]))
            res = max(res, heights[h])
        
        for s, h in stack:
            res = max(res, (len(heights) - s) * h)
        return res