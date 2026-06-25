class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        maxl = height[i]
        maxr = height[j]
        amount = 0

        while i <= j:
            if maxl < maxr:
                amount += maxl - height[i] if maxl-height[i]>0 else 0
                maxl = max(maxl, height[i])
                i+=1
            else:
                amount += maxr - height[j] if maxr-height[j]>0 else 0
                maxr = max(maxr, height[j])
                j-=1
        
        return amount