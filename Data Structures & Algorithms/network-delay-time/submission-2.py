class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        m = defaultdict(list)
        for u,v,t in times:
            m[u].append([v,t])
        
        print(m)
        
        visited = set()
        heap = []
        heapq.heappush(heap, (0, k))
        while heap:
            p, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            if len(visited) == n:
                return p
            for i,j in m[node]:
                heapq.heappush(heap, (p+j,i))

        return -1