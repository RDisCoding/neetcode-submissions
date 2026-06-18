class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        count = 0
        x = 0
        def dfs(r,c):
            nonlocal x
            if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or grid[r][c]==0 or grid[r][c]=="#":
                return
            
            grid[r][c] = "#"
            x +=1
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    print("klnfalkf")
                    x = 0
                    dfs(r,c)
                    print(x)
                    count = max(count, x)

        return count