class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        m = defaultdict(list)
        heap = []
        heapq.heapify(heap)
        for p in points:
            x, y = p[0], p[1]
            m[x**2 + y**2].append(p)
            heapq.heappush(heap, x**2+y**2)
        ans = []
        for i in range(k):
            x = heapq.heappop(heap)
            for j in m[x]:
                ans.append(j)
        
        return ans[:k]

        