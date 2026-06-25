class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        for p in range(len(points)):
            dist = points[p][0]*points[p][0] + points[p][1]*points[p][1]
            heapq.heappush(heap, (dist, points[p]))

        for i in range(k):
            d, p = heapq.heappop(heap)
            res.append(p)
        
        return res