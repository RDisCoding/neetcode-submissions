class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mapping = defaultdict(list)
        for i in range(len(prerequisites)):
            mapping[prerequisites[i][0]].append(prerequisites[i][1])
        
        visit = set()

        def dfs(i):
            if i in visit: 
                return False

            if not mapping[i]: 
                return True
            

            visit.add(i)
            for j in mapping[i]:
                if not dfs(j): 
                    return False
            visit.remove(i)
            mapping[i] = []
            return True

        for i in range(numCourses):
            if not dfs(i): 
                return False
        return True
