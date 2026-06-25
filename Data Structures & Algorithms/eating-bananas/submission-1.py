class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) > h: return -1
        i = 1
        maxr = max(piles)
        while i<maxr: 
            midr = i + (maxr-i)//2
            time = 0
            for p in piles:
                time += math.ceil(p/midr)
            
            if time <= h:
                maxr = midr
            else:
                i = midr+1
        
        return maxr