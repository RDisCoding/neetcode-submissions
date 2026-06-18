class Solution:
    def trap(self, height: List[int]) -> int:
        maxl = height[0]
        maxr = height[-1]
        i = 0
        j = len(height) - 1
        amount = 0
        count = 0
        while i < j:
            maxl = max(height[i], maxl)
            maxr = max(height[j], maxr)
            if maxl < maxr:
                amount = min(maxl, maxr) - height[i]
                if amount > 0:
                    count += amount
                i+=1
            else:
                amount = min(maxl, maxr) - height[j]
                if amount > 0: 
                    count+=amount
                j-=1
        return count