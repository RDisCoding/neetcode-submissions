class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        print(parent)

        def find(n):
            p = parent[n]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]

            return p
        
        def union(p1,p2):
            r1 = find(p1)
            r2 = find(p2)

            if r1 == r2:
                return False
            
            parent[r1] = r2
            return True

        for n1,n2 in edges:
            if not union(n1,n2):
                return [n1,n2]