class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pr = 0
        mi = float('inf')
        
        for i in prices:
            if i < mi:
                mi = i
            pr = max(pr, i - mi)

        return pr