class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        rotten = deque()
        fresh = set()

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    rotten.append([r,c,0])
                elif grid[r][c] == 1:
                    fresh.add((r,c))

        print(rotten)

        def makeRotten(r,c,t):
            if r<0 or c<0 or r>=row or c>=col or grid[r][c] == 2 or grid[r][c] == 0:
                return
            
            grid[r][c] = 2
            t+=1
            rotten.append([r,c,t])

            if (r,c) in fresh:
                fresh.remove((r,c))
            return

        time = 0

        while rotten:
            r,c,t = rotten.popleft()
            print(r,c,t)
            makeRotten(r-1,c,t)
            makeRotten(r+1,c,t)
            makeRotten(r,c-1,t)
            makeRotten(r,c+1,t)
            time = max(time,t)
        
        return time if not fresh else -1