class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0; j = len(height) - 1
        maxl,maxr = height[i],height[j]
        res = 0

        while i<j:
            if maxl < maxr:
                i+=1
                maxl = max(maxl, height[i])
                res += maxl - height[i]
            else:
                j-=1
                maxr = max(maxr, height[j])
                res += maxr - height[j]
            
        return res