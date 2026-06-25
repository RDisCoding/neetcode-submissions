class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")] * (n+1)
        dp[0] = 0

        squares = []
        i = 1
        while i*i <= n:
            squares.append(i*i)
            i+=1
        
        for j in range(1, n+1):
            for sq in squares:
                if sq>j: break
                dp[j] = min(dp[j], dp[j-sq]+1)

        return dp[n]

