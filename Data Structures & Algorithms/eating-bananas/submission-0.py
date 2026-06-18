class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        k = max(piles)
        if h == n: return k
        
        i = 1
        j = k
        while i<=j:
            mid = i + (j-i)//2
            hrs = 0
            for p in piles:
                hrs += math.ceil(p/mid)
            
            if hrs <= h:
                k = mid
                j = mid - 1
            else:
                i = mid + 1
        return k

            

        