class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mx = 0
        i = 0
        j = len(heights)-1
        while i<j:
            print(mx)
            print(j)
            print(i)
            mx = max(mx, (min(heights[i], heights[j])*(j-i)))
            if heights[i] < heights[j]:
                i+=1
            else:
                j-=1
        return mx