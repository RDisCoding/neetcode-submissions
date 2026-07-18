class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost = float("inf")
        profit = 0

        for p in prices:
            cost = min(cost, p)
            if p - cost > 0:
                profit += (p-cost)
                cost = p

        return profit