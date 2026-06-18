class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            premap[crs].append(pre)
        
        print(premap)
        
        res = []
        visit = set()
        completed = set()
        
        def dfs(i):
            if i in visit: return False
            if i in completed: return True

            visit.add(i)
            for j in premap[i]:
                if not dfs(j):
                    return False

            visit.remove(i)
            completed.add(i)
            res.append(i)
            return True
        
        for i in range(numCourses):
            if not dfs(i): 
                return []

        return res