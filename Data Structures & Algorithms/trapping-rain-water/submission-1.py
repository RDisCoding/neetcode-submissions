class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 1, len(height) - 2
        maxl, maxr = height[0], height[-1]
        res = 0
        while l <= r:
            if maxl <= maxr:
                if (maxl - height[l]) > 0:
                    res += maxl - height[l]
                maxl = max(maxl, height[l])
                l+=1
            else:
                if (maxr - height[r]) > 0:
                    res += maxr - height[r]
                maxr = max(maxr, height[r])
                r -= 1
            
        return res