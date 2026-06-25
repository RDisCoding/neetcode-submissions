class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        m = { src: [] for src,dist in tickets }

        tickets.sort()
        for src, dist in tickets:
            m[src].append(dist)
        
        res = ["JFK"]
        def dfs(src):
            if len(res) == len(tickets)+1: 
                return True
            if src not in m:
                return False
            
            temp = list(m[src])
            for i, v in enumerate(temp):
                res.append(v)
                m[src].pop(i)
                if dfs(v): return True
                res.pop()
                m[src].insert(i, v)
            return False

        dfs("JFK")
        return res