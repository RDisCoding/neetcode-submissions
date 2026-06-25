class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        m = { i : [] for i in range(n)}
        for a,b in edges:
            m[a].append(b)
            m[b].append(a)
        
        print(m)
        
        visited = set()
        def dfs(node, parent):
            if node in visited: 
                return False
            
            visited.add(node)
            for i in m[node]:
                if i == parent:
                    continue
                if not dfs(i, node):
                    return False
            return True
            
        if not dfs(0, -1):
            return False

        return len(visited) == n
