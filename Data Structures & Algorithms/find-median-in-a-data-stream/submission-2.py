class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxheap, -num)
        val = -1*heapq.heappop(self.maxheap)
        heapq.heappush(self.minheap, val)

        if len(self.minheap) > len(self.maxheap):
            val = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -val)

    def findMedian(self) -> float:
        if len(self.maxheap) > len(self.minheap):
            return float(-1*self.maxheap[0])
        else:
            return (-1*self.maxheap[0]+self.minheap[0])/2