class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        visited = set()
        res = []
        
        def dfs(i,j):
            if i>=m or j>=n: 
                return
            if i == m-1 and j == n-1:
                res.append(".")
                return
            visited.add((i,j))
            dfs(i+1,j)
            dfs(i,j+1)
        
        dfs(0,0)
        return len(res)
