class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        maxp = 0
        for i in prices:
            if i<low:
                low = i
            else:
                maxp = max(i-low, maxp)
        return maxp