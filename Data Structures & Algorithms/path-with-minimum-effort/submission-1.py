class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # use heap and visited to get the path with min effort 
        # keep track of the max effort with a variable
        rows, cols = len(heights), len(heights[0])
        visited = set()
        heap = [(0, 0, 0)] # effort, i, j

        maxEffort = 0
        directions = [[0,-1], [0,1], [-1,0], [1,0]]
        while heap:
            effort, i, j = heapq.heappop(heap)

            if (i,j) == (rows-1, cols-1): 
                return effort
            if (i,j) in visited: continue
            visited.add((i,j))
            for x,y in directions:
                if i+x < 0 or j+y < 0 or i+x>=rows or j+y>=cols or (i+x, j+y) in visited: continue
                heapq.heappush(heap, (max(effort, abs(heights[i+x][j+y] - heights[i][j])), i+x, j+y))