class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        m = {i: [] for i in range(n)}
        for a,b in edges:
            m[a].append(b)
            m[b].append(a)
        
        print(m)
        
        visited = set()
        components = 0

        def dfs(node):
            visited.add(node)
            for n in m[node]:
                if n not in visited:
                    dfs(n)

        for i in range(n):
            if i not in visited:
                dfs(i)
                components+=1
        
        return components