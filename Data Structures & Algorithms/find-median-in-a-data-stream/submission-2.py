class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []
        
    def addNum(self, num: int) -> None:
        if not self.maxheap: 
            heapq.heappush_max(self.maxheap, num)
            return
        
        if num < self.maxheap[0]:
            heapq.heappush_max(self.maxheap, num)
            if len(self.maxheap) == len(self.minheap): return
            x = heapq.heappop_max(self.maxheap)
            heapq.heappush(self.minheap, x)
        else:
            if not self.minheap:
                heapq.heappush(self.minheap, num)
                return
            heapq.heappush(self.minheap, num)
            if len(self.maxheap) == len(self.minheap): return
            x = heapq.heappop(self.minheap)
            heapq.heappush_max(self.maxheap, x)
        
    def findMedian(self) -> float:
        if len(self.maxheap) > len(self.minheap):
            return self.maxheap[0] 
        elif len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        else:
            return (self.maxheap[0] + self.minheap[0])/2