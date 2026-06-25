class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i = 0
        for p in range(1, len(prices)):
            if (prices[p] - prices[i]) > 0:
                profit = max(profit, prices[p] - prices[i])
            else:
                i = p
        
        return profit
