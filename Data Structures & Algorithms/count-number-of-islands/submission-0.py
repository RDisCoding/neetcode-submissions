class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bt(i,j):
            if i<0 or j<0 or i>= len(grid) or j>=len(grid[0]) or grid[i][j] == "0" or grid[i][j] == "#": 
                return
            
            grid[i][j] = "#"
            bt(i-1, j)
            bt(i+1, j)
            bt(i, j-1)
            bt(i, j+1)
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count +=1
                    bt(i,j)
        
        return count