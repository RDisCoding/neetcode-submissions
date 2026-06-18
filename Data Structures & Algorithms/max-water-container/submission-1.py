class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mx = 0
        i = 0
        j = len(heights)-1
        while i < j:
            mx = max(mx, min(heights[i], heights[j])*(j-i))
            if heights[i]>heights[j]:
                j-=1
            else:
                i+=1

        return mx