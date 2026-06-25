class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap = {i: [] for i in range(numCourses)}
        for c, p in prerequisites:
            premap[c].append(p)
        
        print(premap)
        visited = set()
        completed = []

        def dfs(c):
            if c in visited: return False

            if c in completed:
                return True
            
            visited.add(c)
            for p in premap[c]:
                if not dfs(p):
                    return False
            visited.remove(c)
            premap[c] = []
            completed.append(c)
            return True

        for i in range(numCourses):
            if i in completed: continue
            if not dfs(i):
                return []

        return completed

