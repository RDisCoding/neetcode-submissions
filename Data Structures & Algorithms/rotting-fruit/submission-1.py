class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = []
        visit = set()
        q = deque()

        def addFruit(i,j):
            if (i<0 or j<0 or i==rows or j==cols or grid[i][j]!=1 or (i,j) in visit):
                return
            fresh.pop()
            visit.add((i,j))
            q.append([i,j])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh.append("f")
                elif grid[i][j] == 2:
                    visit.add((i,j))
                    q.append([i,j])   

        time = 0
        while q:
            for i in range(len(q)):
                x,y = q.popleft()
                grid[x][y] = 2
                addFruit(x-1,y)
                addFruit(x+1,y)
                addFruit(x,y-1)
                addFruit(x,y+1)
            time+=1
        if time: time-=1
        return time if not fresh else -1