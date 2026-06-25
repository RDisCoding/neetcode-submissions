class Solution:
    def reorganizeString(self, s: str) -> str:
        # make a heap of (count of char, char)
        # now here's the thing - if a char is appearing more than (s+1)//2 times
        # then its impossible to keep 2 characters separate

        count = Counter(s)
        heap = [[-cnt, ch] for ch,cnt in count.items()]
        res = ""
        heapq.heapify(heap)

        prev = None
        while heap or prev:
            if prev and not heap: 
                return ""
            n, ch = heapq.heappop(heap)
            res += ch
            n+=1
            if prev:
                heapq.heappush(heap, prev)
                prev = None
            if n != 0:
                prev = [n,ch]
        
        return res