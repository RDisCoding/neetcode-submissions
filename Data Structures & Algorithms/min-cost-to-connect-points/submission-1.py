class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        m = {i: [] for i in range(len(points))}

        for i in range(len(points)):
            for j in range(len(points)):
                if i == j: continue
                m[i].append((abs(points[j][0] - points[i][0]) + abs(points[j][1] - points[i][1]), j))
        print(m)
        minheap = [(0,0)]
        visit = set()
        cost = 0
        while minheap:
            dist, pt = heapq.heappop(minheap)
            if pt in visit: continue
            visit.add(pt)
            cost += dist
            if len(visit) == len(points):
                return cost
            for d,p in m[pt]:
                heapq.heappush(minheap, (d, p))
        
