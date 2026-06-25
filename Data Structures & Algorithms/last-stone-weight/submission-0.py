class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            a = heapq.heappop_max(stones)
            if not stones: break
            b = heapq.heappop_max(stones)
            if a == b: 
                continue
            elif a>b: 
                heapq.heappush_max(stones,a-b)
            else:
                heapq.heappush_max(stones, b-a)
            
        if stones:
            return stones[0]
        else:
            return 0