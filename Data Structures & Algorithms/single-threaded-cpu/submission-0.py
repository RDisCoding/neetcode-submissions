class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        indexed_tasks = sorted([tasks[i][0], tasks[i][1], i] for i in range(len(tasks)))
        available = []
        res = []
        current_time = 0
        i = 0
        while len(res) < len(tasks):
            if not available and current_time < indexed_tasks[i][0]:
                current_time = indexed_tasks[i][0]
            
            while i<len(tasks) and indexed_tasks[i][0] <= current_time:
                heapq.heappush(available, (indexed_tasks[i][1], indexed_tasks[i][2]))
                i+=1
                      
            x, y = heapq.heappop(available)
            res.append(y)
            current_time += x
        return res