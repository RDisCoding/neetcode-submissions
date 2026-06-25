class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        pacific, atlantic = set(), set()

        def dfs(i,j, visit, prevHeight):
            if ((i,j) in visit or i<0 or j<0 or i==rows or j==cols or heights[i][j] < prevHeight):
                return

            visit.add((i,j))
            dfs(i-1,j,visit, heights[i][j])
            dfs(i+1,j,visit, heights[i][j])
            dfs(i,j-1,visit, heights[i][j])
            dfs(i,j+1,visit, heights[i][j])
        

        for i in range(cols):
            dfs(0, i, pacific, heights[0][i])
            dfs(rows-1, i, atlantic, heights[rows-1][i])
        
        for i in range(rows):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, cols-1, atlantic, heights[i][cols-1])

        res = []
        for i in range(rows):
            for j in range(cols):
                if (i,j) in pacific and (i,j) in atlantic:
                    res.append([i,j])
        
        return res
            