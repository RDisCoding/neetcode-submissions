class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h :
            return max(piles)
        
        l = 1
        r = max(piles)
        res = r
        while l<=r:
            mid = (l+r)//2
            if self.canFinish(mid, piles) <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res

    def canFinish(self, speed, piles):
        total = 0
        for p in piles:
            total += (p + speed - 1)//speed
        
        return total