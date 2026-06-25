class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = defaultdict(list)

        for x,y in prerequisites:
            premap[x].append(y)
        
        visit = set()

        def dfs(c):
            if c in visit:
                return False

            if premap[c] == []:
                return True
            
            visit.add(c)
            for pre in premap[c]:
                if not dfs(pre): return False
            
            visit.remove(c)
            premap[c] = []
            return True

        for c in range(numCourses):
            if not dfs(c): return False
        
        return True
        
            
