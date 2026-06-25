class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def addRoom(i,j):
            if (i<0 or i==rows or j<0 or j==cols or (i,j) in visit or grid[i][j] == -1):
                return
            
            visit.add((i,j))
            q.append([i,j])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    visit.add((i,j))
                    q.append([i,j])
        
        dist = 0
        while q:
            for i in range(len(q)):
                x,y = q.popleft()
                grid[x][y] = dist
                addRoom(x-1,y)
                addRoom(x+1,y)
                addRoom(x,y-1)
                addRoom(x,y+1)
            dist+=1
        