class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        memo = {}

        def dfs(r,c):
            if (r, c) in memo: return memo[(r, c)]
            if r == rows - 1 and c == cols - 1: 
                return grid[r][c]
            
            if c == cols - 1: 
                res = grid[r][c] + dfs(r+1, c)
            elif r == rows - 1:
                res = grid[r][c] + dfs(r, c+1)
            else:
                res = grid[r][c] + min(dfs(r+1, c), dfs(r, c+1))
            
            memo[(r, c)] = res
            return res
            
        return dfs(0,0)