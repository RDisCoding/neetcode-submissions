class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        heapq.heapify(minheap)

        for x, y in points:
            dist = x*x + y*y
            heapq.heappush(minheap, (dist,x,y))

        ans = []
        for i in range(k):
            d,x,y = heapq.heappop(minheap)
            ans.append([x,y])
        
        return ans
