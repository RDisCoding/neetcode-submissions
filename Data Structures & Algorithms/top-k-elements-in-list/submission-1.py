class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = {}
        for n in nums:
            c[n] = 1 + c.get(n, 0)

        h = []
        for n in c.keys():
            heapq.heappush(h, (c[n], n))
            if len(h) >k:
                heapq.heappop(h)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(h)[1])
        return res