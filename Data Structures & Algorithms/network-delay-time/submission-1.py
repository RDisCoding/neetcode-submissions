class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i: [] for i in range(1, n+1)}
        for x in times:
            graph[x[0]].append((x[1], x[2]))

        print(graph)

        minheap = []
        heapq.heapify(minheap)
        heapq.heappush(minheap, (0, k))

        visited = set()

        while minheap:
            time, node = heapq.heappop(minheap)
            if node in visited: continue
            
            visited.add(node) 
            for nei in graph[node]:
                heapq.heappush(minheap, (nei[1]+time, nei[0]))
            
            if len(visited)==n: 
                return time
            
        return -1 