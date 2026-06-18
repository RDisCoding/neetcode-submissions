class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        mapper = {i: [] for i in range(numCourses)}
        for c, pre in prerequisites:
            mapper[c].append(pre)

        visit = set()
        completed = set()

        res = []

        def dfs(c):
            if c in visit: return False
            if c in completed: return True

            visit.add(c)
            for i in mapper[c]:
                if not dfs(i):
                    return False
            visit.remove(c)
            completed.add(c)
            res.append(c)

            return True
        
        for i in mapper:
            if not dfs(i):
                return []
        
        return res