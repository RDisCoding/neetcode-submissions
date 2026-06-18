class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        area = 0
        while i<j:
            a = min(heights[i],heights[j])*(j-i)
            area = max(a, area)
            if heights[i]> heights[j]:
                j-=1
            else:
                i+=1
        return area