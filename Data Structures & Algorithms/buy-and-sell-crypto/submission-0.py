class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        low = float('inf')
        for p in prices:
            if p < low:
                low = p
            else:
                profit = max(profit, p-low)
        return profit