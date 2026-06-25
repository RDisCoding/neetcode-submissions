class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # range of capacities -> max(weights) to sum(weights)
        # use bs to reach target days
        i = max(weights)
        j = sum(weights)
        total = j
        while i<j:
            cap = i + (j-i)//2
            d = 0
            s = 0
            for w in weights:
                s+=w
                if s == cap:
                    s=0
                    d+=1
                elif s>cap:
                    s=w
                    d+=1
            if s: d+=1
            if d <= days:
                j = cap
            else:
                i = cap + 1
        return i